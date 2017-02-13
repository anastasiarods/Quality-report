import os
import sys
from jinja2 import Environment, FileSystemLoader
from flask import Flask, render_template
import argparse
import pandas as pd

app = Flask(__name__)


PATH = os.getcwd()

TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)
 
 
def render_template_static(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def generate_context(file_name):
    data = pd.read_csv(file_name)

    heading = "This is test data from course"
    title = "Quality report"
    statistics = [{
        'title': 'Gender',
        'image_url': 'graph.jpg',
        'tests': [{
            'name': 'Female',
            'value': '40.3%',
            'status': 'bad'
        }, {
            'name': 'Male',
            'value': '33.3%',
            'status': 'ok'
        }]
    }, {
        'title': 'Gender',
        'image_url': 'graph.jpg',
        'tests': [{
            'name': 'Female',
            'value': '33.3%',
            'status': 'bad'
        }, {
            'name': 'Male',
            'value': '33.3%',
            'status': 'ok'
        }]
    }, {
        'title': 'LS_1',
        'image_url': 'graph.jpg',
        'tests': [{
            'name': 'non-equal to values: [1, 2, 3, 4, 5]',
            'value': '00.1%',
            'status': 'bad'
        }, {
            'name': 'missing data percentage',
            'value': '33.4%',
            'status': 'bad'
        }]
    }]

    overall = {'status_text': 'Dataset is not clear', 'status': 'bad'}
    dataset = file_name

    context = {
        'dataset': dataset,
        'sitetitle': title,
        'heading': heading,
        'statistics': statistics,
        'overall': overall
    }

    return context


 
def create_index_html(file_name):
    fname = "output.html"
    print (file_name)
    context = generate_context(file_name)
    with open(fname, 'w') as f:
        html = render_template_static('index.html', context)
        f.write(html)
 

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-e', '--enviroment', default='dev', choices=['dev', 'prod'])
    parser.add_argument('file_name')
    return parser

 
def main():
    parser = createParser()
    namespace = parser.parse_args (sys.argv[1:])

    if namespace.enviroment =='prod':
        create_index_html(namespace.file_name)

    else:
        @app.route('/')
        def hello():
            context = generate_context(namespace.file_name)
            return render_template(
                'index.html',
                dataset=context['dataset'],
                sitetitle=context['sitetitle'],
                heading=context['heading'],
                statistics=context['statistics'],
                overall=context['overall'])


        app.debug = True
        app.run(host='0.0.0.0', port=int(8000))

########################################
 
if __name__ == "__main__":
    main()
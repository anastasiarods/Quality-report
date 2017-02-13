## Requirements
* Install Python and PIP
* Install Flask: `pip install flask`

## Dev
Run app: `python main.py`


## API Description
* `title`: Website title
* `heading`: Project name
* `dataset`: Dataset
* `statistics`: vector of maps {title: `string`, tests:[{name: `string`, value: `float %`, status: `ok, bad`}]}
* `graphs`: vector of maps {title, image_url `images are stored in static folder`}
* `overall`: map {status_text, status: `ok, bad` }

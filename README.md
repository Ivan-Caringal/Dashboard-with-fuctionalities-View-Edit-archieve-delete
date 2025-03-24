# CBMMS-2.0

## Usage
This website is built with Bootstrap and Sass. It uses Font Awesome for icons.

In order to customize this website, you need to install Node.js. Then, clone this repository and run:

cd GUI-LIB

### Run this to set up
```bash
npm install
```
This will install Bootstrap, Sass, and Font Awesome. To build your CSS files from Sass, run:

```bash
npm run sass:build
```
To watch your Sass files for changes, run:

```bash
npm run sass:watch
```
After running `sass:watch`, stop the process with `Ctrl + C`.

CD..


rm -rf env  # Deletes the broken environment
python -m venv env  # Creates a new one
source env/Scripts/activate  # Activate it

### Install Python
Ensure you have Python installed. If not, download and install it from [python.org](https://www.python.org/downloads/).
pip install pip
### Install Python dependencies
```bash
pip install crispy-bootstrap5
pip install Django
pip install django-ckeditor
pip install django-crispy-forms
pip install django-js-asset
pip install django-multiselectfield
pip install pillow

pip install psycopg
pip install psycopg2
pip install sqlparse
```


```bash
python manage.py runserver
```


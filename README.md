# Create the project directory
# cmd
mkdir Django_Rest_Framework
cd Django_Rest_Framework

# Create a virtual environment to isolate our package dependencies locally
python -m venv myvenv
source emyvnv/bin/activate  # On Windows use `myvenv\Scripts\activate`

# Install Django and Django REST framework into the virtual environment

>pip install django

>pip install pygments

>pip install djangorestframework

>pip install markdown

>pip install django-filter

>pip freeze > requirements.txt

>pip install -r requirements.txt

>pip uninstall -r requirements.txt -y

>pip install -r requirements.txt

>pip list

>myvenv\Scripts\deactivate

# VS Code
>code .

# Set up a new project with a single application
>django-admin startproject app .

// Note the trailing '.' character

>python manage.py startapp core

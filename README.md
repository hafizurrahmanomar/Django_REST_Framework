# Part-01
# Create the project directory
# cmd open
> mkdir Django_Rest_Framework

> cd Django_Rest_Framework

# Create a virtual environment to isolate our package dependencies locally
>python -m venv myvenv

# Mac use 
// source emyvnv/bin/activate 

# On Windows use 

>myvenv\Scripts\activate

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

# Part-02

## Django Commands

Running server
```
python manage.py runserver
```

Creating super users
```
python manage.py createsuperuser
```
Making DB migrations
```
python manage.py makemigrations
```
then,
```
python manage.py migrate
```

## Running PostgreSQL locally on Docker
1. Install `Docker` and `Docker Compose` from official site. (Search on Google)

2. Create a `docker-compose.yml` file at the root of the project

3. Put this in the compose file (you may use your own DB credentials)
```yml
version: '3.8'

services:
  db:
    image: postgres:13
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=mydb
      - POSTGRES_USER=myuser
      - POSTGRES_PASSOWRD=simplepass
      - POSTGRES_HOST_AUTH_METHOD=trust
    ports:
      - "5432:5432"

volumes:
  postgres_data: {}
```

4. Save and run the command `docker-compose up`

## Adding DB connection info on `settings.py`
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',
        'USER': 'myuser',
        'PASSWORD': 'simplepass',
        'HOST': 'localhost',
        'port': '5432'
    }
}
```

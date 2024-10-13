## Setting up

1. Create a virtual environment
```
python -m venv .venv 
```
2. Activate the environment (always activate this while working in this project)
```
source .venv/bin/activate (for Mac/Linux)
.venv\Scripts\Activate.ps1 (for Windows)
```

3. Install required packages
```bash
pip install django
pip install djangorestframework
pip install pygments
```

## Django Commands

1. Running server
```
python manage.py runserver
```

2. Creating super users
```
python manage.py createsuperuser
```
3. Making DB migrations
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
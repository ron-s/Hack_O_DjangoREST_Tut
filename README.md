## Tutorial Setup
#### 1. Clone repo 
#### 2. Make a virtual environment 
- Setup virtual env: 
  - virtualenv -p /usr/local/bin/python3 venv3  
- Activate virtual env: 
  - source venv3/bin/activate 
  
#### 3. Install depencencies with pip
- Install depedencies from requirements.txt: 
  - pip install -r requirements.txt  
  
#### 4. Start server
- In directory with manage.py run this command: 
  - python manage.py runserver 
  - see working endpoint at: [http://localhost:8000/songs/](http://localhost:8000/songs/)
    
## Example file structure of a starter project
Below is what the file structure looked like after running a basic setup found here: [new_project_setup](http://www.django-rest-framework.org/tutorial/quickstart/) 
![tree structure of project](./images_readme/file_structure.png?raw=true "Optional Title")

## Basic building blocks of endpoints 
![tree structure of project](./images_readme/DRFpieces.png?raw=true "Optional Title")

The image above outlines the pieces that need to be in place for an endpoint to work in the DRF assuming that the basic setup of the project has already been done.

## Building models
Models are just representations of what you have in your database. You can build models by hand or if you have existing data in the DB you can use the command below.
- ```python manage.py inspectdb``` --> Will look at the connected database and show the equivilent Django model 
- ```python manage.py inspectdb > example_models.py``` --> This pipes the output into a file that you can then use to set up your models  

## Migrations 
Anytime you change the models in a Django project you need to apply those change to the database so the models and database tables are synced. This is done by making migrations see the commands below for examples of how to make migrations.  
- ```python manage.py makemigrations``` --> sets up the migration file that reflects the changes you're made to the models
- ```python manage.py migrate``` --> applies the migrations that were setup above to the DB

## Serializers 
A way of serializing and deserializing data. This basically means just taking data and turning it into a different format like JSON. Serializers are basically like translators that allow our Django REST API to talk to differnt programs using formats that both understand. A useful way to inspect serializers is to open the Django shell and print the ```repr``` of them. This can be accomplished by using the commands below.
- ```  python manage.py shell``` --> launches shell from command line

Inside shell use the commands below to import our song serializer and then inspect it. Remember to hit enter after each.
```Python 
  from example_app.serializers import SongSerializer 
  from example_app.models import Songs

  serial_instance = SongSerializer()
  print(repr(serial_instance))
  
  # to quit shell
  quit()
```

## Useful DRF shell commands 
- Running development server: ```python manage.py runserver```
- Getting help in command line: ```python manage.py help``` --> will list all commands available in manage.py. See links below for more details.
- Auto generating fixtures for testsing: [Docs for fixtures](http://django-testing-docs.readthedocs.io/en/latest/fixtures.html)
- Auto generating models.py from the command line: [Docs on inspectdb](https://docs.djangoproject.com/en/1.10/howto/legacy-databases/)
- Link to docs for all shell commands: [django command line docs](https://docs.djangoproject.com/en/1.10/ref/django-admin/)


## Filtering querysets in views 
[Filtering_Docs](http://www.django-rest-framework.org/api-guide/filtering/)

## Useful links to docs about views in DRF 
[Generic_Views_Docs](http://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes)
  

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

## Useful DRF shell commands 
- Running development server: ```python manage.py runserver```
- Getting help in command line: ```python manage.py help``` --> will list all commands available in manage.py. See links below for more details.
- Auto generating models.py from the command line: [Docs on inspectdb](https://docs.djangoproject.com/en/1.10/howto/legacy-databases/)
- Link to docs for all shell commands: [django command line docs](https://docs.djangoproject.com/en/1.10/ref/django-admin/)


## Filtering querysets in views 
[Filtering_Docs](http://www.django-rest-framework.org/api-guide/filtering/)

## Useful links to docs about views in DRF 
[Generic_Views_Docs](http://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes)
  

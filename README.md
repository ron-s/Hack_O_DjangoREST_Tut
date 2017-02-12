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

## Models 
A model just represents a table in your database and the attributes of the model class match the fields in that table. By creating a model and then syncing it with the database Django will tell the database to create a table that matches the model you have created in your project. Below is an example of the Songs model that is in our ```example_project/example_app/models.py``` file. 
```Python
from django.db import models

class Songs(models.Model):
    id = models.AutoField(primary_key=True)
    artist_name = models.CharField(max_length=255, default='')
    song_title = models.CharField(max_length=255, default='')
    song_year = models.IntegerField(blank=True, null=True)
    song_lyrics = models.TextField()

    class Meta:
        db_table = 'song_lyrics'
```
Notice how each attribute in the model class has a datatype to which it is assigned. These data types are defined in the ```django.db.models``` module and offer a convienient way to assign data types the values in our models. 
- [Django model field docs](https://docs.djangoproject.com/en/1.10/ref/models/fields/)
- [Django model docs](https://docs.djangoproject.com/en/1.10/ref/models/) --> There is a ton of documentation here that gets into everything you can possibly do with models. 

## Serializers 
A way of serializing and deserializing data. This basically means just taking data and turning it into a different format like JSON or XML. Serializers are basically like translators that allow our Django REST API to talk to different programs using formats that both understand. There are many ways to define a serializer but we have included a simple example using Django's ```ModelSerializer``` class in the ```example_project/example_app/serializers.py``` file. See below. 

```Python 
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Songs
        fields = '__all__'
```
What we're doing is pointing this serializer at the ```Songs``` model we've already created and telling it serialize all of the fields in that model by declaring ```fields = '__all__'``` in the ```Meta``` of the serializer. You could also declare each attribute explicitly if you liked. Follow the instructions below to inspect this serializer in the Django shell. 

- ```  python manage.py shell``` --> launches shell from command line

- Inside shell use the commands below to import our song serializer and then inspect it. Remember to hit return after entering each line.
```Python 
  from example_app.serializers import SongSerializer 
  from example_app.models import Songs

  serial_instance = SongSerializer()
  print(repr(serial_instance))
  
  # to quit shell
  quit()
```
- Example output

  
  


## Views 

## Linking URLs to views
  

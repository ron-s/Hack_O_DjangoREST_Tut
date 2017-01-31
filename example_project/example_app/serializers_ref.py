"""
Use this file as a reference for the different ways to make a serializer

'Serializers allow complex data such as querysets and model instances to be 
converted to native Python datatypes that can then be easily rendered into 
JSON or XML' DRF docs: http://www.django-rest-framework.org/api-guide/relations/

Anytime you want to inspect what a serializer is doing open the manage.py shell 
and take a look using the commands below: 
>>> python manage.py shell 
>>> from example_app.serializers import my_serializer 
>>> from example_app.models import Songs
>>> serializer_instance = my_serializer()
>>> print(repr(my_serializer))

entering the commmands below will show you what the example data looks like 
>>> all_songs = Songs.objects.all()
>>> serialized_songs = my_serializer(all_songs, many=True)

This will print the current repersentation of the serializer and show you what 
it is currently evaluating 
"""

# remember to import the model the serializer needs to be connected to 
from rest_framework import serializers
from . import models

class SongSerializer(serializers.ModelSerializer):
    """
    Using ModelSerializer makes it much easier to set up serialization for
    data. The meta sub class requires at least two values 'model' and 'fields'
    you see below. 

    * by using fields = '__all__' you're telling the serializer to include all 
    model fields in the objects that are passed through it. 
    You could also explictly declare what fields you wanted serialized here if 
    a subset of all the fields in the model are needed.  

    """
    class Meta:
        model = models.Songs
        fields = '__all__'
        # exclude = ('field_name',) --> lets you exclude fields you don't want

# ---------------------------------------------------------------------------------

class ExampleSerializer(serializers.Serializer):
    """
    This serializer is one step down in abstraction from the ModelSerializer above
    here you need to explictly declare each field that needs to be serialized
    with its appropriate data type. The serializers module that is imported has 
    these data types within it. See the docs here: 
    """
    id = serializers.IntegerField(read_only=True)
    artist_name = serializers.CharField()
    song_year = serializers.IntegerField()
    song_lyrics = serializers.CharField()


"""
Testing out serializer in django shell: 

>>> python manage.py shell 
>>> from example_app.serializers import my_serializer 
>>> from example_app.models import Songs
>>> serializer_instance = my_serializer()
>>> print(repr(my_serializer))

>>> all_songs = Songs.objects.all()
>>> serialized_songs = my_serializer(all_songs, many=True)
"""























## Filtering queries by URL parmeters
In this section of the tutorial we'll focus on filltering the data that comes out of our API endpoints based on information that is provided in the request's URL. 

## Two ways to grab URL parameters

#### Using Regex to capture values in URLs 
```Python 
  url('^songsfilter/(?P<song_year>.+)/$', ExampleView.as_view())
```
This is an example of using a Regex capture group to grab anything that comes after the ```songsfilter/``` endpoint. In this case the Regex is matching any characters and using a named group to assign the characters to the ```song_year``` variable. This variable is then passed to the view as a keyword argument and can be used as a value in many of the built in filtering methods Django provides. It's important to note that in this case the endpoint requires something to be entered in the ```song_year``` capture group. Altering what will and won't be matched can be accomplished by altering the Regex in the capture group. 
[link_to_useful_regex_tool](https://regexr.com)


#### Accessing values captured by Regex inside of a view
Now inside the view that is tied to the regex shown above we need to access the ```song_year``` keyword argument. An example of this can be seen in the [view_examples.py](add_link_to_view_examples.py) file and below.
```Python
class ExampleView(generics.ListAPIView):
    serializer_class = serializers.ExampleSerializer

    def get_queryset(self):
        song_year = self.kwargs['song_year']
        return models.Songs.objects.filter(song_year__exact=song_year)
```
In the view above we're overriding the built in ```get_queryset``` method of the ```generics.ListAPIView``` class. Doing this allows us to access the ```song_year``` keyword argument and then return a subset of objects from our ```Songs``` tables filered on that value. Notice how we're accessing ```self.kwargs``` and asking for the  value from the 'song_year' key.  



[Django_docs_on_URLs](https://docs.djangoproject.com/en/1.10/topics/http/urls/)

#### Using a request's query_params attribute to capture querystring arguments



## Filtering queries by URL parmeters
In this section of the tutorial we'll focus on filltering the data that comes out of our API endpoints based on information that is provided in the request's URL. 

### Two possible methods to grab URL parameters

#### Using Regex to capture values in URLs 
```Python 
  url('^songsfilter/(?P<song_year>.+)/$', ExampleView.as_view())
```
This is an example of using Regex to capture a ```song_year``` argument. In this case anything that is entered after the ```songsfilter/``` endpoint will be assinged to ```song_year``` and passed as a key word argument to the ```ExampleView```. You can then access this argument inside of the view and make filtering decicions based on its value. 

```Python
  song_year = self.kwargs['song_year']
```


[Django_docs_on_URLs](https://docs.djangoproject.com/en/1.10/topics/http/urls/)

#### Using a request's ```query_params``` attribute to capture querystring arguments

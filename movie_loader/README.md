## Instructions for loading sample movie data 
This directory contains a csv of sample movie data that we would like to load into our project. In order to do this we must create a model & corresponding DB table, a serializer, a view(that accepts POST requests), and then set up the URL for this view. 

### Creating the model and corresponding database table
A model just represents a table in your database and the attributes of the model class match the fields in that table. 
- Look at the provided film.csv file and create a model that matches it in the example_app/models.py file. Every column name in the csv should have a matching field declared in the Django model with an additonal ```id``` field set as a primary key. 

Your model should look someting like this:
```Python
class Movies(models.Model):
  # creates an auto incrementing id field used as a primary key in the table 
  id = models.AutoField(primary_key=True)
  
  # examples of different model data types
  text_example = models.CharField(max_length=255, default='')
  integer_example = models.IntegerField(blank=True, null=True)
  large_text_example = models.TextField()
  boolean_example = models.BooleanField()
```
- See this link for: [Model field docs](https://docs.djangoproject.com/en/1.10/ref/models/fields/)

### Running migrations and syncing changes
Anytime you make changes to a model in Django you then need to sync these changes with your database. In our case syncing the changes will cause Django to create a ```migration```, which is just a set of commands that get transformed to SQL and apply the changes made in your Django models to the database. 

- Use this command to make migrations: ```python manage.py makemigrations```
- Once the migration is made apply it with this command: ```python manage.py migrate```
- To see what an auto generated migration looks like check in the ```example_app/migrations``` directory.

### Creating a serializer for our model
We now need to create a serializer for our model. Remember that serializers are needed to transform data in and out of different formats that map to our Django models.

- Create a serializer for the ```Movies``` model in the ```example_app/serializers.py``` file using the existing serializer for the ```Songs``` model as an example. 

### Creating a view for our new model
We now need to create a view that allows us to send POST requests adding data to the ```Movies``` model and its matching database table. Use the exisiting views in the ```example_app/views.py``` file as a guide. Feel free to build either a function or class based view. 
- Build a new view in the ```example_app/views.py``` file that will accept POST and GET request. 

### Linking the view to a URL 
Each view needs to be set up with a URL that points to the correct place. You can also set up URLs to accept parameters that will then be passed into your view as arguments. Use the urls in the ```example_app/urls.py``` file as a guide. 
- Set up the URL routing for the newly created view. 

### Seeing if it works 
If everything has been set up correctly we should be able to start our local server and go to the endpoint we created. This takes a bit of time though and it would be really conivient if we could just run a command that will check that the endpoint is working for us. This is where the built in Django test runner is super helpful. 
- Look in the ```example_app/tests.py``` file and find the test class called ```MovieTest```. This is a simple example of how the tests can be set up in your tests.py file. The tests are just checking that both the POST and GET methods are supported by the endpoint you built. 
- Run these tests using this command: ```python manage.py test example_app``` 

### Using the browsable API
One of the great things about the Django REST Framework is the built in functionality that is added when you use its pre-built classes to build endpoints.
- Start the local server by using this command: ```python manage.py runserver```
- Go to this link: [http://localhost:8000/example/movies/](http://localhost:8000/example/movies/)

### Adding data using our POST endpoint
We will now use the endpoint we created to add data to our database. The ```movie_loader/load_movies.py``` file will make the POST calls to the endpoint we created. This is done by reading the csv file and then using the ```requests``` library to make a POST call for each line in the file. 
- You'll need to have a two terminal windows open for this both with your virtual envirnonment activated. 
- In the first terminal run the ```python manage.py runserver``` command. We need to have our server running so we can send the POST calls. 
- In the second terminal run: ```python load_movies.py film.csv``` in the ```movie_loader``` directory.
If everything works you should see the terminal window running the server begin to log a bunch of POST requests. Once this is complete the data has now been entered in our database. If you would like to check that the data is now present open the link to your Django server: [http://localhost:8000/example/movies/](http://localhost:8000/example/movies/) There should now be a bunch of movie data. 

### Further challanges 
Using the basics we have covered think of ways that you could build endpoints that let users filter the movie data in interesting ways. Make a habit of adding tests for these endpoints as you create them. Writing tests can be a pain but they will save you time over the long run. 



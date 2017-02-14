from django.test import TestCase, Client
from . import models as my_models

class SongListTest(TestCase):
    """
    This just checks that the songs endpoint accepts GET requests
    """
    def setUp(self):
        self.c = Client()

    def test_get_request_sends_200(self):
        response = self.c.get("/songs/")
        self.assertEqual(response.status_code, 200)


class MovieTest(TestCase):
    """
    This test checks that you've setup the endpoint to recive GET and POST
    requests and that you have the correct fields in your model. 
    """

    def setUp(self):
        self.c = Client()
        self.movie_model = my_models.Movies
        self.expected_fields = [
        "id", "year", "length", "title", "subject", "actor",
        "actress", "director", "popularity", "awards", "image" 
        ]


    def test_get_request_sends_200(self):
        response = self.c.get("/movies/")
        self.assertEqual(response.status_code, 200)

    def test_post_request_sends_200(self):
        response = self.c.post("/movies/")
        self.assertEqual(response.status_code, 201)

    def test_movie_model_fields_have_correct_numder_of_fields(self):
        """
        If this test fails make sure you have all of the fields seen in 
        'self.expected_fields' in your model.
        """
        actual_fields = [f.name for f in self.movie_model._meta.get_fields()]
        self.assertEqual(len(self.expected_fields), len(actual_fields))

    def test_movie_model_fields_all_lower_case(self):
        """
        If this test fails make sure all of your model field names are lowercase
        and spelled correctly. If you fail this test and then rename your fields
        don't forget about making and running migrations to share the changes 
        in your model with the databse. 

        """
        actual_fields = [f.name for f in self.movie_model._meta.get_fields()]
        zipped_fields = zip(actual_fields, self.expected_fields)      
        
        for field_tup in zipped_fields:
            self.assertEqual(field_tup[0], field_tup[1])



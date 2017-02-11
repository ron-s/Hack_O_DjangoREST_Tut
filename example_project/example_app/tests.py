from django.test import TestCase, Client
from . import models as my_models

class SongListTest(TestCase):

    def setUp(self):
        self.c = Client()

    def test_get_request_sends_200(self):
        response = self.c.get("/songs/")
        self.assertEqual(response.status_code, 200)


class MovieTest(TestCase):
    """
    Right now this set of tests only checks if there is an endpoint
    that takes GET and POST requests at /example/movies/
    """

    def setUp(self):
        self.c = Client()

    def test_get_request_sends_200(self):
        response = self.c.get("/movies/")
        self.assertEqual(response.status_code, 200)

    def test_post_request_sends_200(self):
        response = self.c.post("/movies/")
        self.assertEqual(response.status_code, 200)






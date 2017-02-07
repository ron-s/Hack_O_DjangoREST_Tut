from django.test import TestCase, Client


class SongListTest(TestCase):

    def setUp(self):
        self.c = Client()

    def test_get_request_sends_200(self):
        response = self.c.get("/example/songs/")
        self.assertEqual(response.status_code, 200)





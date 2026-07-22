from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class HomeAuthenticationTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="StrongPassword123!",
        )

    def test_home_page_returns_200(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "myapp/index.html")

    


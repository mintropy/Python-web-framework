from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.views import status


class TestArticle(APITestCase):
    def test_list_article(self) -> None:
        url = reverse("article list")
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

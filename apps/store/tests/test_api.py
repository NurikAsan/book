from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.store.models import Book
from apps.store.serializers import BookSerializer


class TestAPI(APITestCase):
    def setUp(self):
        pass

    def test_get(self):
      book1 = Book.objects.create(name="Book 1", price=25)
      book2 = Book.objects.create(name="Book 2", price=25)

      url = reverse('book-list')
      resp = self.client.get(url)
      self.assertEqual(resp.status_code, status.HTTP_200_OK)
      self.assertEqual(BookSerializer([book1, book2], many=True).data, resp.data)

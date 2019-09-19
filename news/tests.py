from django.contrib.auth.models import User
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase, APIClient
from rest_framework.test import APIRequestFactory

from group.models import Group
from news.models import News


class NewsTests(APITestCase):
    fixtures = ['main']

    def test_authentication_check_without_pass(self):
        response = self.client.get('/news/users_news/')
        assert response.status_code == 403
        self.assertEqual(response.data, {"detail": "Authentication credentials were not provided."})

    def test_authentication_with_pass(self):
        self.assertTrue(self.client.login(username='test', password='test123testqwerty'))
        response = self.client.get('/news/users_news/')
        self.assertEqual(response.status_code, 200)

    def test_get_users_news(self):
        self.assertTrue(self.client.login(username='test', password='test123testqwerty'))
        response = self.client.get('/news/users_news/')
        self.assertEqual(len(response.data), 4)

    def test_post_news(self):
        self.assertTrue(self.client.login(username='testuser1', password='Vesper582'))
        # response = self.client.get('/news/')
        # self.assertEqual(len(response.data), 4)

        data = {'group': 3, 'title': "bla", 'text': "bla", }
        response = self.client.post('/news/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(News.objects.count(), 1)
        # self.assertEqual(Account.objects.get().name, 'DabApps')

    def test_unsubscribe(self):
        self.assertTrue(self.client.login(username='test', password='test123testqwerty'))
        response = self.client.post('/subscription/', json={"group": 88})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_check_user_news(self):
        new_test = News.objects.get(title="ad")
        self.assertEqual(new_test.group_id, 3)

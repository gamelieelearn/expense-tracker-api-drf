# Create your tests here.

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken


class JWTAuthTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')

    def test_expense_list_authenticated(self):
        response = self.client.get(reverse('expense-list'))
        self.assertEqual(response.status_code, 200)

    def test_expense_list_unauthenticated(self):
        self.client.credentials()  # Remove authentication
        response = self.client.get(reverse('expense-list'))
        self.assertEqual(response.status_code, 401)

"""
Tests user app views.
"""
from main.models import User
from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus

class ModelTests(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(email='testmail@mail.com', password='mypass3342')
        return super().setUp()

    def test_load_register_page(self):
        """Test that registration page loads successfully."""
        response = self.client.get(reverse('user:register'))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'register.html')

    def test_register_new_user_successfully(self):
        """Test that registration is successfull."""
        post_data = {
            'name': 'testname',
            'email': 'test@mail.com',
            'password1': 'asset3726acf',
            'password2': 'asset3726acf'
        }
        response = self.client.post(reverse('user:register'), post_data)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('main:home'))

    def test_load_login_page(self):
        """Test that login page loads successfully."""
        response = self.client.get(reverse('user:login'))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'login.html')

    def test_load_user_successfully(self):
        """Test that registration is successfull."""
        post_data = {
            'email': self.user.email,
            'password': 'mypass3342'
        }
        response = self.client.post(reverse('user:login'), post_data)

        # self.assertTrue(response.context['user'].is_active)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('main:home'))
        


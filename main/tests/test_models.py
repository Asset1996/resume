"""
Tests form current app models
"""
from django.test import TestCase
from main.models import User

class ModelTests(TestCase):

    def test_create_user(self):
        """Test creating a new user with email and password."""
        email = 'test@mail.com'
        password = 'test2233'
        user = User.objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_superuser(self):
        """Test creating a new superuser with email and password."""
        email = 'super@mail.com'
        password = 'test2233'
        user = User.objects.create_superuser(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_normalize_email(self):
        """Test to ensure that email normalizing is working."""
        emails = (
            ('teST@mail.Com', 'teST@mail.com',),
            ('tEsT2@mAIl.COM', 'tEsT2@mail.com',),
        )

        for email, expected_email in emails:
            user = User.objects.create_user(email=email)
            self.assertEqual(user.email, expected_email)

    def test_new_user_without_email_raises_value_error(self):
        """
        Test to ensure that creating new 
        user without email raises value error.
        """
        with self.assertRaises(ValueError):
            User.objects.create_user(email='')

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(password='pass', email='email@email.com'):
    """Create a sample user"""
    return get_user_model().objects.create_user(password, email)


class ModelTests(TestCase):

    def test_create_new_user_sucessful(self):
        """Test creating a new user is sucessful"""

        password = "password"
        email = "test@test.com"
        user = get_user_model().objects.create_user(
            password=password,
            email=email
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = "email@TEST.com"
        user = get_user_model().objects.create_user(email, '1234')

        self.assertEqual(user.email, email.lower())

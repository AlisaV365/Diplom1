from rest_framework import status
import random
from django.conf import settings
from django.core import mail
from django.test import TestCase
from django.urls import reverse
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
from users.views import RegisterView, ProfileView, generate_new_password


class ViewTest(TestCase):

    def setUp(self) -> None:
        pass

    def test_form_valid(self):
        data = {
            'email': 'testuser@example.com',
        }
        response = self.client.post(
            '/users:register/',
            data=data
        )

        self.assertEqual(
            User.objects.count(),
            0
        )
        self.assertEqual(
            len(mail.outbox),
            0
        )


class ProfileViewTest(TestCase):
    def setUp(self) -> None:
        pass


    def test_post_form(self):
        data = {
            'email': 'newemail@example.com',
        }
        response = self.client.post(
            '/users:profile/',
            data=data
        )


class RegisterViewTest(TestCase):
    def test_form_invalid(self):
        data = {
            'email': 'invalidemail',
        }
        response = self.client.post(
            reverse('users:register'),
            data=data
        )
        self.assertFormError(
            response, 'form', 'email', 'Введите правильный адрес электронной почты.')

import random
from django.conf import settings
from django.core import mail
from django.test import TestCase
from django.urls import reverse
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
from users.views import RegisterView, ProfileView, generate_new_password


class RegisterViewTest(TestCase):

    def test_form_valid(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword',
        }
        response = self.client.post(reverse('users:register'), data=form_data)
        self.assertRedirects(response, reverse('users:register'))
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Поздравляем с регистрацией')
        self.assertEqual(mail.outbox[0].to, ['testuser@example.com'])


class ProfileViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser', email='testuser@example.com')
        self.client.force_login(self.user)

    def test_get_object(self):
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object'], self.user)

    def test_post_form(self):
        form_data = {
            'username': 'newusername',
            'email': 'newemail@example.com',
        }
        response = self.client.post(reverse('users:profile'), data=form_data)
        self.assertRedirects(response, reverse('users:profile'))
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'newusername')
        self.assertEqual(self.user.email, 'newemail@example.com')


class GenerateNewPasswordTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser', email='testuser@example.com')

    def test_generate_new_password(self):
        response = self.client.get(reverse('users:generate_new_password'))
        self.assertRedirects(response, reverse('catalog:index'))
        self.user.refresh_from_db()
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Вы сменили пароль')
        self.assertTrue(self.user.check_password(mail.outbox[0].message().get_payload()))

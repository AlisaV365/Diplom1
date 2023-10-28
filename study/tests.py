from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse


from study.models import Lesson, Test, Question, Answer, UserAnswer
from users.models import User


class StudyTestCase(APITestCase):
    def setUp(self) -> None:
        pass

    def test_create_lesson(self):
        """Тестирование создания уроков"""
        data = {
            'name': 'test',
            'description': 'test description'
        }
        response = self.client.post(
            '/add_lesson/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_list_lesson(self):
        """Тестирование вывода списка уроков"""

        Lesson.objects.create(
            id=1,
            name='test',
            description='test description',
            image='test image',
            urlvideo='test url'
        )

        response = self.client.get(
            '/lessons/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


class TestTest(APITestCase):
    def setUp(self):
        data = {
            'name': 'test',
            'description': 'test description'
        }
        response = self.client.post(
            '/test_delete/',
            data=data
        )

    def test_delete_test(self):
        data = {
            'name': 'test',
            'description': 'test description'
        }
        response = self.client.post(
            '/test_delete/',
            data=data
        )

        self.assertFalse(
            Test.objects.all().exists()
        )

    def test_create_test(self):
        """Test creation testing """
        data = {
            'name': 'test',
            'description': 'test description'
        }
        response = self.client.post(
            '/add_test/',
            data=data
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Test.objects.all().count(), 1)
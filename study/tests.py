from rest_framework import status
from rest_framework.test import APITestCase

from study.models import Lesson


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

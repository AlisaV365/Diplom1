from django.db import models
from users.models import User

from users.models import NULLABLE

"""модель уроки"""


class Lesson(models.Model):
    name = models.CharField(max_length=350, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='media/catalog/', verbose_name='картинка', **NULLABLE)
    urlvideo = models.URLField(max_length=200, verbose_name='ссылка на видео', **NULLABLE)

    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


"""модель тесты"""


class Test(models.Model):
    name = models.CharField(max_length=350, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    test_id = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True,
                                related_name='lesson', verbose_name='урок')

    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'тест'
        verbose_name_plural = 'тесты'


"""модель вопросы"""


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name='Тест', related_name='questions')
    text = models.CharField(max_length=500, verbose_name='Текст вопроса')

    def __str__(self):
        return f'Вопрос {self.test}'

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'


"""модель ответы"""


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Ответ')
    text = models.CharField(max_length=500, verbose_name='Текст ответа')

    def __str__(self):
        return f'Ответ {self.question}'

    class Meta:
        verbose_name = 'ответ'
        verbose_name_plural = 'ответы'


"""модель вопросы пользователя"""


class UserAnswer(models.Model):
    answer = models.CharField(max_length=400, verbose_name='Текст овтета')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Вопрос', related_name='user_answera')
    is_passed = models.BooleanField(default=False, verbose_name="Введен")

    def __str__(self):
        return f'{self.user} {self.question} {self.answer}'

    class Meta:
        verbose_name = 'ответ_пользователя'
        verbose_name_plural = 'ответы_пользователя'

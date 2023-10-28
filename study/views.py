from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from study.models import Lesson, Test, Question, UserAnswer, Answer
from study.serializers import LessonSerializer, TestSerializer, QuestionSerializer, QuestionWithAnswerSerializer, \
    UserAnswerSerializer, AnswerSerializer


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    """Получение списка материалов.
       Есть фильтр и поиск по имени материала."""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    filter_backends = [DjangoFilterBackend]
    ordering_fields = ['name', 'description']
    filterset_fields = ('name', 'description')


class LessonDetailAPIView(generics.RetrieveAPIView):
    """Получение конкретного материала."""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()



class LessonUpdateAPIView(generics.UpdateAPIView):
    """Обновление материала."""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()



class LessonDeleteAPIView(generics.DestroyAPIView):
    """Удаление материала."""
    queryset = Lesson.objects.all()

class TestCreateAPIView(generics.CreateAPIView):
    """Создание теста.
       Для создания теста необходимо ввести имя теста и описание."""
    serializer_class = TestSerializer

class TestListAPIView(generics.ListAPIView):
    """Получение списка тестов.
       Есть фильтр и поиск по имени теста и уроку."""
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    filter_backends = [DjangoFilterBackend]
    ordering_fields = ['name', 'lesson']
    filterset_fields = ('name',)


class TestDetailAPIView(generics.RetrieveAPIView):
    """Получение конкретного теста."""
    serializer_class = TestSerializer
    queryset = Test.objects.all()

class TestUpdateAPIView(generics.UpdateAPIView):
    """Обновление теста."""
    serializer_class = TestSerializer
    queryset = Test.objects.all()

class TestDeleteAPIView(generics.DestroyAPIView):
    """Удаление теста."""
    queryset = Test.objects.all()


class QuestionCreateAPIView(generics.CreateAPIView):
    """Создание вопроса.
       Для создания вопроса необходимо ввести тест вопроса."""
    serializer_class = QuestionSerializer

class QuestionListAPIView(generics.ListAPIView):
    """Получение списка вопросов.
       Есть фильтр и поиск по тесту."""
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    filter_backends = [DjangoFilterBackend]
    ordering_fields = ['test']
    filterset_fields = ('test',)


class QuestionDetailAPIView(generics.RetrieveAPIView):
    """Получение конкретного вопроса.
       Если пользователь уже отвечал на этот вопрос, то будет выведен также ответ пользователя."""
    queryset = Question.objects.all()

    def get_serializer_class(self):
        if UserAnswer.objects.filter(question=self.get_object().pk, user=self.request.user.pk).exists():
            return QuestionWithAnswerSerializer
        else:
            return QuestionSerializer


class QuestionUpdateAPIView(generics.UpdateAPIView):
    """Обновление вопроса."""
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

class QuestionDeleteAPIView(generics.DestroyAPIView):
    """Удаление вопроса."""
    queryset = Question.objects.all()


class UserAnswerCreateAPIView(generics.CreateAPIView):
    """Создание ответа пользователя на вопрос.
       Для создания ответа необходимо ввести текст."""
    serializer_class = UserAnswerSerializer

    def perform_create(self, serializer):
        new_ans = serializer.save()
        question = Question.objects.get(pk=new_ans.question.pk)
        correct_answer = Answer.objects.get(question=question.pk)
        if new_ans.answer.lower() == correct_answer.text.lower():
            new_ans.is_passed = True
        elif new_ans.answer.lower() != correct_answer.text.lower():
            new_ans.is_passed = False
        new_ans.user = self.request.user
        new_ans.save()


class UserAnswerDeleteAPIView(generics.DestroyAPIView):
    """Удаление ответа пользователя."""
    queryset = UserAnswer.objects.all()


class AnswerCreateAPIView(generics.CreateAPIView):
    """Создание правильного ответа на вопрос.
       Для создания ответа необходимо ввести текст ответа."""
    serializer_class = AnswerSerializer

class AnswerUpdateAPIView(generics.UpdateAPIView):
    """Обновление правильного ответа на вопрос."""
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

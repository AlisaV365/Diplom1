from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import LessonCreateAPIView, LessonUpdateAPIView, LessonDeleteAPIView, \
    LessonDetailAPIView, LessonListAPIView, TestCreateAPIView, TestListAPIView, TestDetailAPIView, TestUpdateAPIView, \
    TestDeleteAPIView, QuestionCreateAPIView, QuestionListAPIView, QuestionDetailAPIView, QuestionUpdateAPIView, \
    QuestionDeleteAPIView, AnswerCreateAPIView, AnswerUpdateAPIView, UserAnswerCreateAPIView, UserAnswerDeleteAPIView
from study.apps import StudyConfig

app_name = StudyConfig.name


router = DefaultRouter()

urlpatterns = [
    path('add_lesson/', LessonCreateAPIView.as_view(), name='add_lesson'),
    path('lessons/', LessonListAPIView.as_view(), name='lessons'),
    path('lessons/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson'),
    path('lessons/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lessons/delete/<int:pk>/', LessonDeleteAPIView.as_view(), name='lesson_delete'),
    path('', include(router.urls)),
    path('lesson/detail/<int:pk>', LessonDetailAPIView.as_view(), name='lesson_detail'),
    path('study/', include(router.urls)),
    # test
    path('add_test/', TestCreateAPIView.as_view(), name='add_test'),
    path('tests/', TestListAPIView.as_view(), name='tests'),
    path('tests/<int:pk>/', TestDetailAPIView.as_view(), name='test'),
    path('tests/update/<int:pk>/', TestUpdateAPIView.as_view(), name='test_update'),
    path('tests/delete/<int:pk>/', TestDeleteAPIView.as_view(), name='test_delete'),

    # question
    path('add_question/', QuestionCreateAPIView.as_view(), name='add_question'),
    path('questions/', QuestionListAPIView.as_view(), name='questions'),
    path('questions/<int:pk>/', QuestionDetailAPIView.as_view(), name='question'),
    path('questions/update/<int:pk>/', QuestionUpdateAPIView.as_view(), name='question_update'),
    path('questions/delete/<int:pk>/', QuestionDeleteAPIView.as_view(), name='question_delete'),

    # answer
    path('add_answer/', AnswerCreateAPIView.as_view(), name='add_answer'),
    path('answers/update/<int:pk>/', AnswerUpdateAPIView.as_view(), name='answer_update'),

    # user_answer
    path('add_user_answer/', UserAnswerCreateAPIView.as_view(), name='add_user_answer'),
    path('user_answer/delete/<int:pk>/', UserAnswerDeleteAPIView.as_view(), name='user_answer_delete'),
]



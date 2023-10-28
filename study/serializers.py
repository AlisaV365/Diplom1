from rest_framework import serializers
from .models import Lesson, Test, Question, UserAnswer, Answer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    question_count = serializers.SerializerMethodField()
    right_answers = serializers.SerializerMethodField()
    questions = QuestionSerializer(read_only=True, many=True)

    def get_question_count(self, test):
        return Question.objects.filter(test=test.pk).count()

    def get_right_answers(self, test):
        current_user = self.context['request'].user
        right_answers = 0
        questions = Question.objects.filter(test=test.pk)
        for question in questions:
            try:
                if UserAnswer.objects.filter(question=question.pk, user=current_user).last().is_passed:
                    right_answers += 1
            except AttributeError:
                pass
        return right_answers

    class Meta:
        model = Test
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    test = TestSerializer(read_only=True, many=True)
    test_count = serializers.SerializerMethodField()

    def get_test_count(self, test_id):
        return Test.objects.filter(test_id=test_id.pk).count()

    class Meta:
        model = Lesson
        fields = '__all__'


class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = '__all__'


class QuestionWithAnswerSerializer(serializers.ModelSerializer):
    user_answers = UserAnswerSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

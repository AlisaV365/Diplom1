from django.contrib import admin

from study.models import Lesson, Test, Question, Answer, UserAnswer


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'urlvideo',)
    list_filter = ('name',)
    search_fields = ('name', 'description',)


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    list_filter = ('name',)
    search_fields = ('name', 'description',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('test', 'text',)
    list_filter = ('test',)
    search_fields = ('text',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'text',)
    list_filter = ('question',)
    search_fields = ('text',)

@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('answer', 'is_passed',)
    list_filter = ('is_passed',)
    search_fields = ('answer',)
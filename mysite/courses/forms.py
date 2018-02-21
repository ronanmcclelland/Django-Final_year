from django import forms
from .models import Course, Lesson


class LessonForm(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = ['lesson_title', 'document_upload']

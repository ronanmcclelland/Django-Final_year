from django import forms
from .models import Course, Lesson, Document


class LessonForm(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = ['lesson_title', 'lesson_description']


class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ['document_title', 'document_upload']


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['courseName', 'field', 'course_logo', 'shortDesc', 'courseDesc']

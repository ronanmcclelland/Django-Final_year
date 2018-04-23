from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.fields import GenericRelation
from fav.models import Favorite


class Course(models.Model):
    user = models.ForeignKey(User)
    courseName = models.CharField(max_length=200)
    field = models.CharField(max_length=100)
    course_logo = models.FileField()
    shortDesc = models.CharField(max_length=100, default='')
    courseDesc = models.CharField(max_length=500)
    favorites = GenericRelation(Favorite)

    def __str__(self):
        return self.courseName


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson_title = models.CharField(max_length=200)
    lesson_description = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.lesson_title


class Document(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    document_title = models.CharField(max_length=200)
    document_upload = models.FileField(default='')

    def __str__(self):
        return self.document_title



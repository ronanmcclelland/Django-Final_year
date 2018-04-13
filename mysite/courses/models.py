from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission, User


class Course(models.Model):
    user = models.ForeignKey(User)
    courseName = models.CharField(max_length=200)
    length = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    course_logo = models.FileField()
    courseDesc = models.CharField(max_length=500)

    def __str__(self):
        return self.courseName + ' - ' + self.length


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson_title = models.CharField(max_length=200)
    document_upload = models.FileField(default='')
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.lesson_title



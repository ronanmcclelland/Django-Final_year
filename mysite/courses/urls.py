from django.conf.urls import url, include
from . import views

app_name = 'courses'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^all-courses/$', views.all_courses, name='all-courses'),
    url(r'^create_course/$', views.create_course, name='course-add'),
    url(r'^(?P<course_id>[0-9]+)/create_lesson/$', views.create_lesson, name='create_lesson'),
    url(r'^(?P<course_id>[0-9]+)/(?P<lesson_id>[0-9]+)/create_document/$', views.create_document, name='create_document'),
    url(r'^(?P<course_id>[0-9]+)/delete_course/$', views.delete_course, name='delete_course'),
    url(r'^(?P<course_id>[0-9]+)/(?P<lesson_id>[0-9]+)/(?P<document_id>[0-9]+)/delete_document/$', views.delete_document, name='delete_document'),
    url(r'^(?P<course_id>[0-9]+)/(?P<lesson_id>[0-9]+)/delete_lesson/$', views.delete_lesson, name='delete_lesson'),
    url(r'^(?P<course_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^search/$', views.search, name='search'),
    url(r'^(?P<course_id>[0-9]+)/(?P<lesson_id>[0-9]+)/$', views.lesson_detail, name='lesson_detail'),
    url(r'^all/(?P<course_id>[0-9]+)/$', views.other_detail, name='other_detail'),
]


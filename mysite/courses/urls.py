from django.conf.urls import url, include
from . import views

app_name = 'courses'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create_course$', views.create_course, name='course-add'),
    url(r'^(?P<course_id>[0-9]+)/create_lesson/$', views.create_lesson, name='create_lesson'),
    url(r'^(?P<course_id>[0-9]+)/delete_course/$', views.delete_course, name='delete_course'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]


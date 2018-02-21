from django.conf.urls import url, include
from . import views

app_name = 'accounts'

urlpatterns = [
    # /accounts/
    url(r'^student-register/$', views.StudentRegView.as_view(), name='studentregiter'),
    url(r'^teacher-register/$', views.TeacherRegView.as_view(), name='teacherregiter'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
]

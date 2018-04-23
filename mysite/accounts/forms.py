from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['first_name', 'surname', 'username', 'email', 'password', 'password_confirm']

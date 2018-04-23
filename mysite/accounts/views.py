from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views import generic
from django.views.generic import View
from .forms import UserForm
from courses.models import Course


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                courses = Course.objects.filter(user=request.user)
                return render(request, 'courses/index.html', {'courses': courses})
            else:
                return render(request, 'accounts/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'accounts/login.html', {'error_message': 'Invalid login'})
    return render(request, 'accounts/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        confirm_pass = form.cleaned_data['password_confirm']
        if password == confirm_pass:
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
        else:
            return render(request, 'accounts/register.html', {'error_message': 'Password no work', 'form': form})
        if user is not None:
            if user.is_active:
                login(request, user)
                course = Course.objects.filter(user=request.user)
                return render(request, 'courses/index.html', {'courses': course})
    context = {
        "form": form,
    }
    return render(request, 'accounts/register.html', context)


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'accounts/login.html', context)


class StudentRegView(View):
    form_class = UserForm
    template_name = 'accounts/student-form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.ser_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('courses:index')

        return render(request, self.template_name, {'form': form})


class TeacherRegView(View):
    form_class = UserForm
    template_name = 'accounts/teacher-form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.ser_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('courses:index')

        return render(request, self.template_name, {'form': form})

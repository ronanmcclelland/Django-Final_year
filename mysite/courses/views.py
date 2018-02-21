from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Course, Lesson
from django.db.models import Q
from .forms import LessonForm


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'accounts/login.html')
    else:
        courses = Course.objects.filter(user=request.user)
        lesson_results = Lesson.objects.all()
        query = request.GET.get("q")
        if query:
            courses = courses.filter(
                Q(courseName__icontains=query) |
                Q(field__icontains=query)
            ).distinct()
            lesson_results = lesson_results.filter(
                Q(lesson_title__icontains=query)
            ).distinct()
            return render(request, 'courses/index.html', {
                'courses': courses,
                'lessons': lesson_results,
            })
        else:
            return render(request, 'courses/index.html', {'courses': courses})


def create_lesson(request, course_id):
    form = LessonForm(request.POST or None, request.FILES or None)
    course = get_object_or_404(Course, pk=course_id)
    if form.is_valid():
        course_lesson = course.lesson_set.all()
        for s in course_lesson:
            if s.lesson_title == form.cleaned_data.get("lesson_title"):
                context = {
                    'course': course,
                    'form': form,
                    'error_message': 'You already added that lesson',
                }
                return render(request, 'courses/create_song.html', context)
        lesson = form.save(commit=False)
        lesson.course = course
        lesson.save()
        return render(request, 'courses/detail.html', {'courses': course})
    context = {
        'course': course,
        'form': form,
    }
    return render(request, 'courses/create_lesson.html', context)


def delete_course(request, course_id):
    course1 = Course.objects.get(pk=course_id)
    course1.delete()
    courses1 = Course.objects.filter(user=request.user)
    return render(request, 'course/index.html', {'courses': courses1})


class DetailView(generic.DetailView):
    model = Course
    template_name = 'courses/detail.html'


class CourseCreate(CreateView):
    model = Course
    fields = ['courseName', 'length', 'field', 'course_logo', 'courseDesc']

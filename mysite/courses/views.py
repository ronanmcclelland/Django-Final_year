from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Course, Lesson, Document
from django.db.models import Q
from .forms import LessonForm, CourseForm, DocumentForm


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


def all_courses(request):
    courses = Course.objects.all()
    return render(request, 'courses/all-courses.html', {'courses': courses})


def create_course(request):
    if not request.user.is_authenticated():
        return render(request, 'courses/login.html')
    else:
        form = CourseForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            course = form.save(commit=False)
            course.user = request.user
            course.save()
            return render(request, 'courses/detail.html', {'course': course})
        context = {
            "form": form,
        }
        return render(request, 'courses/create_course.html', context)


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
                return render(request, 'courses/create_lesson.html', context)
        lesson = form.save(commit=False)
        lesson.course = course
        lesson.save()
        return render(request, 'courses/lesson.html', {'course': course, 'lesson': lesson})
    context = {
        'course': course,
        'form': form,
    }
    return render(request, 'courses/create_lesson.html', context)


def create_document(request, course_id, lesson_id):
    form = DocumentForm(request.POST or None, request.FILES or None)
    course = get_object_or_404(Course, pk=course_id)
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    if form.is_valid():
        course_lesson_document = lesson.document_set.all()
        for s in course_lesson_document:
            if s.document_title == form.cleaned_data.get("document_title"):
                context = {
                    'course': course,
                    'lesson': lesson,
                    'form': form,
                    'error_message': 'You already added that document',
                }
                return render(request, 'courses/create_document.html', context)
        document = form.save(commit=False)
        lesson.course = course
        document.lesson = lesson
        document.save()
        return render(request, 'courses/lesson.html', {'course': course, 'lesson': lesson, 'document': document})
    context = {
        'course': course,
        'lesson': lesson,
        'form': form,
    }
    return render(request, 'courses/create_document.html', context)


def delete_course(request, course_id):
    course1 = Course.objects.get(pk=course_id)
    course1.delete()
    courses1 = Course.objects.filter(user=request.user)
    return render(request, 'courses/index.html', {'courses': courses1})


def delete_document(request, course_id, lesson_id, document_id):
    course = Course.objects.get(pk=course_id)
    lesson = Lesson.objects.get(pk=lesson_id)
    doc1 = Document.objects.get(pk=document_id)
    doc1.delete()
    docs1 = get_object_or_404(Lesson, pk=lesson_id)

    return render(request, 'courses/lesson.html', {'course': course, 'lesson': lesson, 'document': docs1})


def delete_lesson(request, course_id, lesson_id):
    course = Course.objects.get(pk=course_id)
    lesson = Lesson.objects.get(pk=lesson_id)
    lesson.delete()
    lessons = get_object_or_404(Course, pk=course_id)

    return render(request, 'courses/detail.html', {'course': course, 'lesson': lessons})


def detail(request, course_id):
    if not request.user.is_authenticated():
        return render(request, 'accounts/login.html')
    else:
        user = request.user
        course = get_object_or_404(Course, pk=course_id)
        if course.user == user:
            return render(request, 'courses/detail.html', {'course': course, 'user': user, 'object': course})
        else:
            return render(request, 'courses/other-detail.html', {'course': course, 'user': user})


def lesson_detail(request, course_id, lesson_id):
    if not request.user.is_authenticated():
        return render(request, 'accounts/login.html')
    else:
        user = request.user
        course = get_object_or_404(Course, pk=course_id)
        lesson = get_object_or_404(Lesson, pk=lesson_id)
        return render(request, 'courses/lesson.html', {'course': course, 'user': user, 'lesson': lesson})


def other_detail(request, course_id):
    if not request.user.is_authenticated():
        return render(request, 'accounts/login.html')
    else:
        user = request.user
        course = get_object_or_404(Course, pk=course_id)
        return render(request, 'courses/other-detail.html', {'course': course, 'user': user})


def search(request):
    if request.method == 'GET':
        course_name = request.GET.get('search')
        courses = Course.objects.filter(courseName__icontains=course_name)
        if courses:
            return render(request, "courses/search.html", {"courses": courses})
        else:
            return render(request, "accounts/login.html", {})
    else:
        return render(request, "accounts/login.html", {})

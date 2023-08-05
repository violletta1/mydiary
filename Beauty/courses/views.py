from django.shortcuts import render
from django.views import generic as views

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import user_passes_test

from Beauty.accounts.decorators import is_allowed_group_user, is_admin_group_user,is_practitioner_group_user,is_client_group_user
from Beauty.common.forms import CommentForm
from Beauty.courses.models import Course
from Beauty.courses.forms import CourseForm, CourseDeleteForm, CourseEditForm

# Create your views here.



@login_required()
def list_courses(request):
    is_practitioner = is_practitioner_group_user(request.user)
    courses = Course.objects.all().order_by('-created_at')
    context = {'courses':courses,'is_practitioner':is_practitioner}
    return render(request, template_name='courses/courses_list.html', context=context)

def course_search(request):
    query = request.GET.get('q')
    if query:
        results = Course.objects.filter(title__icontains=query)
    else:
        results = None

    return render(request, 'courses/courses_search_results.html', {'results': results})
#NOTES


@user_passes_test(is_practitioner_group_user)
@login_required()
def create_course(request):
    # is_practitioner = is_practitioner_group_user(request.user)
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.user = request.user
            course.save()
            return redirect('list_courses')
    else:
        form = CourseForm()
    contex = {'form':form,}
    return render(request, 'courses/course_create.html', contex)



@login_required()
def details_course(request,pk):
    course = Course.objects.get(pk=pk)
    comment_form = CommentForm()
    is_practitioner = is_practitioner_group_user(request.user)
    user_who_created_it = course.user
    user = request.user
    context = {
        'current_user': user,
        'course': course,
        'user_who_created_it': user_who_created_it,
        'is_practitioner': is_practitioner,
        "likes": course.like_set.count(),
        "comments": course.comment_set.all(),
        "comment_form": comment_form,

    }
    return render(request, template_name='courses/course_details.html', context=context)

@user_passes_test(is_practitioner_group_user)
@login_required()
def edit_course(request,pk):
    course = Course.objects.get(pk=pk)
    form = CourseEditForm(instance=course)

    if request.user != course.user:
        return redirect('no_access')

    if request.method == "POST":
        form = CourseEditForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('details_course', pk=pk)

    context = {
        "course": course,
        "form": form,

    }

    return render(request, 'courses/edit_course.html', context)

@user_passes_test(is_practitioner_group_user)
@login_required()
def delete_course(request,pk):
    course = Course.objects.filter(pk=pk).get()
    form = CourseDeleteForm(request.POST or None, instance=course)
    if request.user != course.user:
        return redirect('no_access')
    if form.is_valid():
        form.save()
        return redirect('list_courses')
    context = {
        'form': form, 'course': course
    }
    return render(request, 'courses/course_delete.html', context=context)


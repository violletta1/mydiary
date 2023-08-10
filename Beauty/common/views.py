from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.models import Group
from Beauty.accounts.decorators import is_admin_group_user
from Beauty.common.forms import CommentForm
from Beauty.common.models import Like, Comment
from Beauty.courses.models import Course
from Beauty.diary.models import Post, Note
from Beauty.treatments.models import Treatment
from django.views import generic as views
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


UserModel = get_user_model()
def index(request):
    return render(request,template_name='base.html')


def about(request):
    return render(request, template_name='common/about.html')


class NoAccessView(TemplateView):
    template_name = 'no_access.html'


class UserListView(LoginRequiredMixin,UserPassesTestMixin,views.ListView,):
    model = UserModel
    template_name = 'common/user_list.html'  # Replace with your template name

    def test_func(self):
        return self.request.user.is_staff
    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy('no_access'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = context['object_list']


        user_data = []
        for user in users:
            user_courses = Course.objects.filter(user=user)
            user_posts = Post.objects.filter(user=user)
            user_notes = Note.objects.filter(user=user)
            user_treatments = Treatment.objects.filter(user=user)

            user_data.append({
                'user': user,
                'courses': user_courses,
                'posts': user_posts,
                'notes': user_notes,
                'treatments': user_treatments,
            })

        context['user_data'] = user_data
        return context

@login_required
def like_functionality(request, course_id):
    course = Course.objects.get(pk=course_id)
    kwargs = {
        'to_course': course,
        'user': request.user
    }

    like_object = Like.objects \
        .filter(**kwargs) \
        .first()

    if like_object:
        like_object.delete()
    else:
        new_like_object = Like(**kwargs)
        new_like_object.save()

    return redirect(request.META['HTTP_REFERER'] + f"#{course_id}")


@login_required
def comment_functionality(request, model, model_id):
    if model == 'course':
        instance = get_object_or_404(Course, pk=model_id)
    elif model == 'treatment':
        instance = get_object_or_404(Treatment, pk=model_id)
    elif model == 'post':
        instance = get_object_or_404(Post, pk=model_id)
    else:
        # Handle invalid model name here (if needed)
        return redirect('index')  # Redirect to a suitable URL


    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment_instance = form.save(commit=False)
            if model == 'course':
                new_comment_instance.to_course = instance
            elif model == 'treatment':
                new_comment_instance.to_treatment = instance
            elif model == 'post':
                new_comment_instance.to_post = instance

            new_comment_instance.user = request.user  # Set the user field before saving
            new_comment_instance.save()

        # Redirect back to the course detail page with the course_id as the anchor link
        return redirect(f"{request.META['HTTP_REFERER']}#{model_id}")

    # Handle the GET request or invalid form submission
    return redirect(request.META['HTTP_REFERER'])

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    # Check if the user is the owner of the comment or if they have the necessary permission to delete it
    if request.user == comment.user:
        comment.delete()

    # Redirect back to the previous page
    return redirect(f"{request.META['HTTP_REFERER']}#{comment_id}")



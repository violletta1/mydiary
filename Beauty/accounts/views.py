from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login, get_user_model
from django.contrib.auth.models import Group
from Beauty.accounts.forms import RegisterUserForm, BeautyUserForm, BeautyUserEditForm, DeleteBeautyUserForm
from Beauty.accounts.models import BeautyUser
from Beauty.courses.models import Course
from Beauty.diary.models import Note, Post
from Beauty.treatments.models import Treatment

UserModel = get_user_model()



class RegisterUserView(views.FormView):
    template_name = 'accounts/register-page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        group_id = form.cleaned_data['group']
        group = Group.objects.get(pk=group_id)
        user = form.save()
        user.groups.add(group)

        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     context['next'] = self.request.GET.get('next', '')
    #
    #     return context
    #
    # def get_success_url(self):
    #     return self.request.POST.get('next', self.success_url)


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'



class LogoutUserView(auth_views.LogoutView):
    pass


class ProfileDetailsView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel
    profile_image = static('images/logo.png')

    def get_profile_image(self):
        if self.object.profile_picture is not None:
            return self.object.profile_picture
        return self.profile_image

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object  # Get the current user from the view's context

        user_notes = Note.objects.filter(user=user).order_by('-created_at')
        courses = Course.objects.all().order_by('-created_at')
        treatments = Treatment.objects.filter(user=user).order_by('-created_at')
        user_posts = Post.objects.filter(user=user).order_by('-created_at')

        context['user_notes'] = user_notes  # Add the user_notes to the context
        context['user_posts'] = user_posts
        context['courses'] = courses  # Add the user_notes to the context
        context['treatments'] = treatments
        context['profile_image'] = self.get_profile_image()

        return context


class ProfileEditView(views.UpdateView):
    model = UserModel
    form_class = BeautyUserEditForm
    template_name = 'accounts/profile-edit-page.html'
    def get_object(self, **kwargs):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('profile_details', args=[self.request.user.pk])


class ProfileDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    form_class = DeleteBeautyUserForm
    success_url = reverse_lazy("index")

    def get_object(self, **kwargs):
        return self.request.user

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['username'].initial = self.request.user.get_username()
        return form

    def form_invalid(self, form):
        form.add_error("password", "Invalid password")
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.request.user.delete()
        return HttpResponseRedirect(success_url)


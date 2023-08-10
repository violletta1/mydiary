
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from Beauty.diary.models import Post,Note
from django.contrib.auth import get_user_model
from .forms import PostForm, PostEditForm, PostDeleteForm, NotesForm, NoteEditForm, NoteDeleteForm, \
    PostPractitionerForm, PostClientForm, PostEditPractitionerForm, PostEditClientForm
from django.contrib.auth import mixins as auth_mixins
from django.views import generic as views
from django.urls import reverse, reverse_lazy
from Beauty.accounts.decorators import is_allowed_group_user, is_admin_group_user,is_practitioner_group_user,is_client_group_user
from ..common.forms import CommentForm

UserModel = get_user_model()

@login_required
def create_post(request):
    is_practitioner = is_practitioner_group_user(request.user)
    is_client = is_client_group_user(request.user)
    is_admin = is_admin_group_user(request.user)

    # if is_admin:
    #     form = PostForm()
    #     if request.method == 'POST':
    #         form = PostForm(request.POST)
    if is_practitioner:
        form = PostPractitionerForm()
        if request.method == 'POST':
            form = PostPractitionerForm(request.POST)
    else:
        form = PostClientForm()
        if request.method == 'POST':
            form = PostClientForm(request.POST)

    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        return redirect('post_list')
    context = {
            'form': form
        }
    return render(request, 'diary/posts/create_post.html', context=context)

    # if is_admin:
    #     form = PostForm(request.POST or None)
    # elif is_practitioner:
    #     form = PostPractitionerForm(request.POST or None)
    # else :
    #     form = PostClientForm(request.POST or None)
    #
    # if form.is_valid():
    #     form.instance.user = request.user
    #     post = form.save(commit=False)
    #
    #     post.save()
    #     return redirect('post_list')
    # context = {
    #         'form':form
    #     }
    # return render(request, 'diary/posts/create_post.html', context=context)

    # if is_practitioner:
    #     form = PostPractitionerForm()
    #     if request.method == 'POST':
    #         form = PostPractitionerForm(request.POST)
    #         if form.is_valid():
    #             form.instance.user = request.user
    #             post = form.save(commit=False)
    #
    #             post.save()
    #             return redirect('post_list')
    #     context = {
    #         'form':form
    #     }
    # elif is_client:
    #     form = PostClientForm()
    #     if request.method == 'POST':
    #         form = PostClientForm(request.POST)
    #         if form.is_valid():
    #             post = form.save(commit=False)
    #             post.user = request.user
    #             post.save()
    #             return redirect('post_list')
    #     context = {
    #         'form': form
    #     }
    # else:
    #     form = PostClientForm()
    #     context = {
    #         'form': form
    #     }
    #
    # return render(request, 'diary/posts/create_post.html', context=context)





def post_list(request):
    posts = Post.objects.all()
    return render(request,template_name='diary/posts/post_list.html', context={'posts':posts})


def post_details(request,pk):
    post = Post.objects.get(pk=pk)
    comment_form = CommentForm()
    is_admin = is_admin_group_user(request.user)
    context = {
        'is_admin': is_admin,
        'post': post,
        'comments': post.comment_set.all(),
        'comment_form': comment_form,
        'likes': post.like_set.count(),
    }

    return render(request, template_name='diary/posts/post_details.html', context=context)



@login_required
def delete_post(request, pk):
    post = Post.objects.filter(pk=pk).get()
    form = PostDeleteForm(request.POST or None, instance=post)
    is_admin = is_admin_group_user(request.user)
    if not is_admin:
        if request.user != post.user:
            return redirect('no_access')
    if form.is_valid():
        form.save()
        return redirect('post_list')
    context = {
        'form':form, 'post':post
    }
    return render(request,'diary/posts/delete_post.html', context=context)


@login_required
def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    is_practitioner = is_practitioner_group_user(request.user)
    is_client = is_client_group_user(request.user)
    is_admin = is_admin_group_user(request.user)
    if not is_admin:
        if request.user != post.user:
            return redirect('no_access')
    if is_practitioner or is_admin:
        form = PostEditPractitionerForm(instance=post)
    else:
        form = PostEditClientForm(instance=post)
    if (is_practitioner or is_admin) and request.method == "POST":
        form = PostEditPractitionerForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_details', pk=pk)
    elif is_client and request.method == 'POST':
        form = PostEditClientForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_details', pk=pk)

    context = {
        "post": post,
        "form": form,
    }

    return render(request, 'diary/posts/edit_post.html', context)


def post_search(request):
    query = request.GET.get('q')
    if query:
        results = Post.objects.filter(title__icontains=query)
    else:
        results = None

    return render(request, 'diary/posts/post_search_results.html', {'results': results})


#NOTES
class NotesList(auth_mixins.LoginRequiredMixin,auth_mixins.UserPassesTestMixin,views.DetailView):
    template_name = 'diary/notes/notes_list.html'
    model = UserModel

    def test_func(self):
        # Check if the logged-in user is the owner of the notes
        user = self.get_object()
        return self.request.user == user

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy('no_access'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.object  # Get the current user from the view's context
        # Get the notes related to the current user and order them by created_at (or any other suitable field)
        user_notes = Note.objects.filter(user=user).order_by('-created_at')

        context['user_notes'] = user_notes  # Add the user_notes to the context

        return context


@login_required
def notes_search(request):
    query = request.GET.get('q')
    if query:
        results = Note.objects.filter(title__icontains=query)
    else:
        results = None

    return render(request, 'diary/notes/notes_search_results.html', {'results': results})


@login_required
def notes_create(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user  # Associate the note with the current logged-in user
            note.save()
            # form.save()
            return redirect(reverse('notes_list', args=[request.user.pk]))  # Replace 'post_list' with the URL name for the list view of all posts
    else:
        form = NotesForm()
    return render(request, 'diary/notes/note_create.html', {'form': form})


@login_required
def note_edit(request, pk):
    note = Note.objects.get(pk=pk)
    form = NoteEditForm(instance=note)
    user_creator = note.user
    if request.user != user_creator:
        return redirect('no_access')

    if request.method == "POST":
        form = NoteEditForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_details', pk=pk)

    context = {
        "note": note,
        "form": form,
    }

    return render(request, 'diary/notes/edit_notes.html', context)


@login_required
def note_details(request,pk):
    note = Note.objects.get(pk=pk)
    user_creator = note.user
    if request.user != user_creator:
        return redirect('no_access')
    context = {'note':note}
    return render(request, template_name='diary/notes/note_details.html', context=context)


@login_required
def delete_note(request,pk):
    note = Note.objects.get(pk=pk)
    form = NoteDeleteForm(request.POST or None, instance=note)
    user_creator = note.user
    if request.user != user_creator:
        return redirect('no_access')
    if request.method == 'POST':
        if form.is_valid():
            note.delete()
            return redirect(reverse('notes_list', args=[request.user.pk]))
    context = {
        'form':form, 'note':note
    }
    return render(request,'diary/notes/delete_note.html', context=context)


    # post = Post.objects.filter(pk=pk).get()
    # form = PostDeleteForm(request.POST or None, instance=post)
    # if form.is_valid():
    #     form.save()
    #     return redirect('post_list')
    # context = {
    #     'form':form, 'post':post
    # }
    # return render(request,'posts/delete_post.html', context=context)
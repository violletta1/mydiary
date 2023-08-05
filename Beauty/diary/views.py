
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from Beauty.diary.models import Post,Note
from django.contrib.auth import get_user_model
from .forms import PostForm, PostEditForm,PostDeleteForm,NotesForm,NoteEditForm,NoteDeleteForm
from django.contrib.auth import mixins as auth_mixins
from django.views import generic as views
from django.urls import reverse
from Beauty.accounts.decorators import is_allowed_group_user, is_admin_group_user,is_practitioner_group_user,is_client_group_user
from ..common.forms import CommentForm

UserModel = get_user_model()

@login_required
def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_list')
    context = {
        'form':form
    }
    return render(request, 'diary/posts/create_post.html', context=context)




def post_list(request):
    posts = Post.objects.all()
    return render(request,template_name='diary/posts/post_list.html', context={'posts':posts})


def post_details(request,pk):
    post = Post.objects.get(pk=pk)
    comment_form = CommentForm()
    is_practitioner = is_practitioner_group_user(request.user)
    context = {
        'post': post,
        'comments': post.comment_set.all(),
        'comment_form': comment_form,
        'likes': post.like_set.count(),
        'is_practitioner': is_practitioner,
    }

    return render(request, template_name='diary/posts/post_details.html', context=context)



@login_required
@user_passes_test(is_practitioner_group_user)
def delete_post(request, pk):
    post = Post.objects.filter(pk=pk).get()
    form = PostDeleteForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    context = {
        'form':form, 'post':post
    }
    return render(request,'diary/posts/delete_post.html', context=context)


@login_required
@user_passes_test(is_practitioner_group_user)
def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    form = PostEditForm(instance=post)

    if request.method == "POST":
        form = PostEditForm(request.POST, instance=post)
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
class NotesList(auth_mixins.LoginRequiredMixin,views.DetailView):
    template_name = 'diary/notes/notes_list.html'
    model = UserModel

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
    context = {'note':note}
    return render(request, template_name='diary/notes/note_details.html', context=context)


@login_required
def delete_note(request,pk):

    note = Note.objects.get(pk=pk, user=request.user)
    form = NoteDeleteForm(request.POST or None, instance=note)
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
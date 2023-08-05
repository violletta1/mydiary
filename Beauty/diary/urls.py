from django.urls import path,include
from Beauty.diary import views
from Beauty.diary.views import NotesList

urlpatterns = [

    path('note_create/', views.notes_create, name='note_create'),
    path('notes_list/<int:pk>', NotesList.as_view(), name='notes_list'),
    path('notes_search/', views.notes_search, name='notes_search'),
    path('note_details/<int:pk>', include([
        path('', views.note_details, name='note_details'),
        path('edit/', views.note_edit, name='note_edit'),
        path('delete/', views.delete_note, name='delete_note')])),

    path('create_post/', views.create_post, name='post_create'),
    path('post_search/', views.post_search, name='post_search'),
    path('post_list/', views.post_list, name='post_list'),
    path('post_details/<int:pk>', include([
        path('', views.post_details, name='post_details'),
        path('edit/', views.post_edit, name='post_edit'),
        path('delete/', views.delete_post, name='delete_post')])),
]
from django.urls import path,include
from .views import list_courses, create_course, details_course, edit_course, delete_course, \
    course_search
urlpatterns = [
    path('create_courses/',create_course, name='create_course'),
    path('courses_search/', course_search, name='course_search'),
    path('list_courses/', list_courses, name='list_courses'),
    path('details/<int:pk>', details_course, name='details_course'),
    path('edit/<int:pk>', edit_course, name='edit_course'),
    path('delete/<int:pk>', delete_course, name='delete_course'),
]


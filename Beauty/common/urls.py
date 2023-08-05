from django.urls import path
from .views import index, about,like_functionality,comment_functionality,NoAccessView


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('noaccess/', NoAccessView.as_view(), name='no_access'),
    path('like/<int:course_id>', like_functionality, name="like"),
    path('comment/<str:model>/<int:model_id>/', comment_functionality, name="comment"),
    # ... your other URL patterns ...
    path('comment/<str:model>/<int:course_id>/', comment_functionality, name='comment_course'),
    path('comment/<str:model>/<int:treatment_id>/', comment_functionality, name='comment_treatment'),
    path('comment/<str:model>/<int:post_id>/', comment_functionality, name='comment_post'),

]
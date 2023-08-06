from django.urls import path,include
from .views import index, about,like_functionality,comment_functionality,NoAccessView,delete_comment


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('noaccess/', NoAccessView.as_view(), name='no_access'),
    path('like/<int:course_id>', like_functionality, name="like"),
    path('comment/<str:model>/<int:model_id>/',include([
        path('', comment_functionality, name="comment")
        ,
    ])),
    path('delete/<int:comment_id>', delete_comment, name="comment_delete")

]
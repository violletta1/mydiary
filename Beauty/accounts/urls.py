from django.urls import path, include
from .views import RegisterUserView, LoginUserView, LogoutUserView, \
        ProfileEditView, ProfileDeleteView, ProfileDetailsView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name="register_user"),
    path('login/', LoginUserView.as_view(), name="login_user"),
    path('logout/', LogoutUserView.as_view(), name="logout_user"),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='profile_details'),
        path('edit/', ProfileEditView.as_view(), name='profile_edit'),
        path('delete/', ProfileDeleteView.as_view(), name='profile_delete')
    ]))
]


from django.urls import path
from .views import SignUpView, LoginView, UpdateProfileView, ProfileView, LogoutView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile-update/', UpdateProfileView.as_view(), name='profile-update'),
    path('logout/', LogoutView.as_view(), name='logout')
]
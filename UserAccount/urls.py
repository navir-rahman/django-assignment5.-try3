from django.urls import path
from .views import UserRegistrationView, UserLoginView, custom_logout, ChangePasswordForm, UserUpdateView
urlpatterns = [
    path('signup/', UserRegistrationView.as_view(), name='signUp'),
    path('singIn/', UserLoginView.as_view(), name='signIn'),
    path('singOut/',custom_logout , name='signOut'),
    path('profile/',UserUpdateView.as_view() , name='profile'),
    path('password_change/',ChangePasswordForm.as_view() , name='password_change'),
]

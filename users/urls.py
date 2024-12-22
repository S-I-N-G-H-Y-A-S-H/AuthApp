from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('signup/',views.signup_view,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='/users/login'),name='logout'),
    path('profile/',views.profile,name='profile')
]

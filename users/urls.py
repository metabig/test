from django.urls import path

from blog.models import Post
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('login/', views.userLogin.as_view(), name="login"),
    path('logout/', views.userLogout.as_view(), name="logout"),
]

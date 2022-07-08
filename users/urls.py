from django.urls import path
from django.conf.urls import url
from blog.models import Post
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('login/', views.userLogin.as_view(), name="login"),
    path('logout/', views.userLogout.as_view(), name="logout"),
    url(r'^signup/$', views.signup, name='signup'),
    url('login/account_activation_sent/', views.account_activation_sent,
        name='account_activation_sent'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
]

from django.urls import path
from django.conf.urls import url
from blog.models import Post
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetView, PasswordResetCompleteView, PasswordChangeDoneView
urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('login/', views.userLogin.as_view(), name="login"),
    path('logout/', views.userLogout.as_view(), name="logout"),
    url(r'^signup/$', views.signup, name='signup'),
    url('login/account_activation_sent/', views.account_activation_sent,
        name='account_activation_sent'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),

    # Change Password
    path('password_reset/', PasswordResetView.as_view(
        template_name="login/reset_password.html"), name='password_reset'),
    path('password_reset/done/', PasswordResetCompleteView.as_view(template_name="login/reset_password_done.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="login/password_change_form.html"),
         name='password_reset_confirm'),
    path('reset/done/', PasswordResetDoneView.as_view(template_name="login/password_change_done.html"),
         name='password_reset_complete'),
    path('password_change/', PasswordChangeView.as_view(
        template_name="login/password_change_form.html"), name='password_change'),
]

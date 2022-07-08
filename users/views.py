from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView


# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'login/signup.html', {
#         'form': form
#     })

def profile(request):
    return render(request, 'login/profile.html')


class userLogin(LoginView):
    template_name = 'login/login.html'


class userLogout(LogoutView):
    template_name = 'login/logout.html'

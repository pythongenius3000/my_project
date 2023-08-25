from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy


# Create your views here.
#def login(request):
 #   return render(request, 'app_auth/login.html')

#def profile(request):
 #   return render(request, 'app_auth/profile.html')

def register(request):
    return render(request, 'app_auth/register.html')

def login_view(request):
    redirect_url = reverse('profile')
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None: #если пользователь прошел аутентификацию
        login(request, user)
        return redirect(redirect_url)
    return render(request, 'app_auth/login.html', {"error": "Пользователь не найден."})

@login_required(login_url=reverse_lazy('login')) #необходимость в аутентификацие
def profile_view(request):
    return render(request, 'app_auth/profile.html')

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))
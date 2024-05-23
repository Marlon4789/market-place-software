from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError
from django.contrib.auth.models import User


def home(request):
    return render(request, 'content/home.html')

def exit(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request):
    return render(request, 'content/profile.html')



def register(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html', {"form": CustomUserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], 
                    email=request.POST["email"],
                    password=request.POST["password1"])
                user.save()
                auth_login(request, user)
                return redirect('profile')
            except IntegrityError:
                error_message = "Este usuario ya está registrado."
                return render(request, 'registration/register.html', {"form": CustomUserCreationForm, "error": error_message})
        else:
            error_message = "Las contraseñas no coinciden."
            return render(request, 'registration/register.html', {"form": CustomUserCreationForm, "error": error_message})


def login_view(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            error_message = "Nombre de usuario o contraseña incorrectos."
            return render(request, 'registration/login.html', {"form": AuthenticationForm, "error": error_message})

        auth_login(request, user)
        return redirect('profile')
    
def password_reset(request):
    return render(request, 'registration/password_reset_form.html')



# Reestablecer contraseña
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/reset_password_form.html'

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/reset_password_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/reset_password_confirm.html'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/reset_password_complete.html'

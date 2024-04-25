from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError
from django.contrib.auth.models import User


# Create your views here.

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
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                auth_login(request, user)
                return redirect('profile')
            except IntegrityError:
                error_message = "Este usuario ya está registrado."
                return render(request, 'registration/register.html', {"form": CustomUserCreationForm, "error": error_message})
        else:
            error_message = "Las contraseñas no coinciden."
            return render(request, 'registration/register.html', {"form": CustomUserCreationForm, "error": error_message})
#    data = {
#        'form': CustomUserCreationForm()
#    }
#    if request.method == 'POST':
#        user_creation_form = CustomUserCreationForm(data=request.POST)
       
#        if user_creation_form.is_valid():
#            user_creation_form.save()

#            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
#            auth_login(request, user)
#            return redirect('profile')
#    return render(request, 'registration/register.html', data)



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
    # return render(request, 'registration/login.html')

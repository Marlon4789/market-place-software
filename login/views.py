from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm

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
   data = {
       'form': CustomUserCreationForm()
   }
   if request.method == 'POST':
       user_creation_form = CustomUserCreationForm(data=request.POST)
       
       if user_creation_form.is_valid():
           user_creation_form.save()

           user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
           auth_login(request, user)
           return redirect('profile')
   return render(request, 'registration/register.html', data)



def login_view(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'registration/login.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        auth_login(request, user)
        return redirect('profile')
    # return render(request, 'registration/login.html')

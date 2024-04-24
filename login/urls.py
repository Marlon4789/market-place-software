from django.urls import path, include
from .views import profile, home, exit, register, login_view

urlpatterns = [
    path('', home, name='home'),
    path('profile/', profile, name='profile'),
    path('logout/', exit, name='exit'),

    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
]

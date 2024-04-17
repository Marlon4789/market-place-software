from rest_framework import serializers
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


# Register users
class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=100,
        style={'placeholder': 'Username', 'autofocus': True}
    )
    email = serializers.EmailField(
        max_length=100,
        style={'placeholder': 'Email'}
    )
    password = serializers.CharField(
        max_length=100,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    confirm_password = serializers.CharField(
        max_length=100,
        style={'input_type': 'password', 'placeholder': 'Confirm Password'}
    )

    def validate(self, data):
        """
        Check that the passwords match.
        """
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        """
        Create a new user instance.
        """
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        # Redirigir al usuario a la vista de inicio de sesión después de crear un nuevo usuario
        return redirect(reverse('login'))












# from django.contrib.auth.models import User
# from rest_framework import serializers


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username','email', 'password']
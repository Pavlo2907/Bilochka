from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Subject

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    pass

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_active', 'is_staff']



from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from django import forms

from .models import Task, Profile


# -Register an user
    
class CreateUserForm(UserCreationForm):
    
    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']


# - Login an user

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# - Create a task

class CreateTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'content','priority']
        exclude = ['user',]

   

# - Update an user

class UpdateUserForm(forms.ModelForm):

    password = None

    class Meta:
        model = User
        fields = ['username', 'email',]
        exclude = ['password1', 'password2',]
        

# - Update a profile picture

class UpdateProfileForm(forms.ModelForm):
    
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-file'}))


    class Meta:

        model = Profile

        fields = ['profile_pic',]
















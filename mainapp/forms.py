from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class registrationForm(UserCreationForm):
    password1=forms.CharField(label="password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(label="confirm password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name', 'email','number']
        widgets={
            "username":forms.TextInput(attrs={"class": "form-control"}),
            "first_name":forms.TextInput(attrs={"class": "form-control"}),
            "last_name":forms.TextInput(attrs={"class": "form-control"}),
            "email":forms.TextInput(attrs={"class": "form-control"}),  
            "number":forms.TextInput(attrs={"class": "form-control"}),                                         
        }

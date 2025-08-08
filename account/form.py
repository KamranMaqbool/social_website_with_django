from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, required=True, label='Password')


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput
    )
    class Meta:
        model = get_user_model()
        fields = ["username", "first_name", "email"]

    # This method is calling when is_valid() method call in view.py file while registering
    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Password don't match")
        return cd["password2"]
    
    def clean_email(self):
        data = self.cleaned_data["email"]
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("User with this email already exist")
        return data


class UserEditForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email"]
        
    def clean_email(self):
        data = self.cleaned_data["email"]
        qs = User.objects.exclude(
            id=self.instance.id
        ).filter(
            email=data
        )
        if qs.exists():
            raise forms.ValidationError('Email already in use.')
        return data

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["date_of_birth", "photo"]
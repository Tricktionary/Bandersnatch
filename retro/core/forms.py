from .models import *
from django import forms
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils.safestring import mark_safe


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email',
            'password'
        ]
        labels = {
            'email': 'Email',
            'password': 'Password'
        }
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            print('email existed')
            raise forms.ValidationError('Email is already in use.')
        if email in [None, '']:
            raise forms.ValidationError('Please enter an email')
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters long.')
        return password

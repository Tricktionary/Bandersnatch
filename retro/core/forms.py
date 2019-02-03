from .models import *
from django import forms
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils.safestring import mark_safe


def serialized_form_errors(form):
    errors = dict([(key, [str(error) for error in value]) for key, value in form.errors.items()])
    return JsonResponse({'errors': errors, })

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

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        labels = {
            'email': 'Email',
            'password': 'Password',
        }
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email does not correspond to an account.')
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise forms.ValidationError('Password is at least 8 characters long.')
        return password

    def clean(self):
        cleaned_data = super(LogInForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if email and password:
            if User.objects.filter(email=email).exists():
                user = User.objects.get(email=email)
                if not user.check_password(password):
                    error = forms.ValidationError('Incorrect password.')
                    self.add_error('password', error)

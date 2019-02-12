from django.conf import settings
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from ..forms import LoginForm, serialized_form_errors

def login_page(request):
    loginForm = LoginForm(
        request.POST or None,
    )
    context={
        "login_form":loginForm
    }
    return render(request, 'core/login.html', context=context)

def login_submit(request):
    print(request.POST)
    login_form = LoginForm(request.POST)

    if login_form.is_valid():
        MAX_USERNAME_LENGTH = 30
        email = login_form.cleaned_data.get('email')
        username = email[0:MAX_USERNAME_LENGTH]
        password = login_form.cleaned_data.get('password')
        
        user = authenticate(request=request, username=username, email=email, password=password)
        if user is not None:
            login(request, user)

        return HttpResponse(200)

    else:
        error_json = serialized_form_errors(login_form)
        return error_json
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from ..forms import LoginForm

def login_page(request):
    loginForm = LoginForm(
        request.POST or None,
    )
    context={
        "login_form":loginForm
    }
    return render(request, 'core/login.html', context=context)
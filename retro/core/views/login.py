from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

def login_page(request):
    return render(request, 'core/login.html', context={})
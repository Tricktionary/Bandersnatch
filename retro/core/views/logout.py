from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from django.contrib.auth import logout


def logout_user(request):
    logout(request)
    return render(request, 'core/landing_page.html', context={})
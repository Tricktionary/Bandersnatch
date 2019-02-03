from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

def stage(request):
    return render(request, 'core/stage.html', context={})
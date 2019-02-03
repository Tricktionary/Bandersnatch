from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .decorators import authenticated_as_player

@authenticated_as_player
def stage(request):
    return render(request, 'core/stage.html', context={})
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

def home_page(request):
    if request.user.is_authenticated:
        return redirect('/stage')

    return render(request, 'core/landing_page.html', context={})

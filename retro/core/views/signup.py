from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from ..forms import SignUpForm

def signup_page(request):
    
    signup_form = SignUpForm(
        request.POST or None,
    )

    context = {
        'signup_form': signup_form
    }
    return render(request, 'core/signup.html', context=context)
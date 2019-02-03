from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from ..forms import SignUpForm,serialized_form_errors
from ..models import *

def signup_page(request):
    
    signup_form = SignUpForm(
        request.POST or None,
    )

    context = {
        'signup_form': signup_form
    }
    return render(request, 'core/signup.html', context=context)

def signup_submit(request):
    print(request.POST)
    signup_form = SignUpForm(request.POST)

    if signup_form.is_valid():
        email = signup_form.cleaned_data.get('email')
        password = signup_form.cleaned_data.get('password')
        user = create_user(email, password)
        print('signup was valid')
    
        if user is not None:
            player = create_player(user, email)
            game = create_new_game(player)
            login(request, user)
        else:
            print('USER WAS NONE ')
    else:
        error_json = serialized_form_errors(signup_form)
        return error_json
    response = HttpResponse(200)
    response.delete_cookie('segment_anonymous_id')
    return response

def create_user(email, password):
    email = email.lower()
    MAX_USERNAME_LENGTH = 30
    username = email[0:MAX_USERNAME_LENGTH]
    user = User.objects.create_user(username, email, password)
    user.save()
    user = authenticate(username=username, email=email, password=password)

    return user

def create_player(user, email):
    player = Player.objects.create(user=user, email=email)
    return player

def create_new_game(player):
    stage = Stage.objects.get(root=True)
    game = Game.objects.create(player=player,stage=stage,end=False)
    game.save()
    return game
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .decorators import authenticated_as_player

from ..models import *
@authenticated_as_player
def stage(request):
    player = Player.objects.get(user=request.user)
    game = Game.objects.get(player=player,game_number=player.game_number)
    stage = game.stage

    if stage.end_stage == False:
        choice_a = Choice.objects.get(stage=stage,choice_a=True)
        choice_b = Choice.objects.get(stage=stage,choice_b=True)
        
        context={
            'stage_description':stage.description,
            'choice_a_description':choice_a.description,
            'choice_b_description':choice_b.description,
        }
    else:
        context={
            'stage_description':stage.description,
            'choice_a_description':"",
            'choice_b_description':"",
        }
    return render(request, 'core/stage.html', context=context)

def stage_a(request):
    player = Player.objects.get(user=request.user)
    game = Game.objects.get(player=player)
    stage = game.stage
    
    next_stage = Stage.objects.get(id=game.stage.stage_b.id)
    game.stage = next_stage
    game.save()

    if next_stage.end_stage == False:
        choice_a = Choice.objects.get(stage=stage,choice_a=True)
        choice_b = Choice.objects.get(stage=stage,choice_b=True)
        
        context={
            'stage_description':stage.description,
            'choice_a_description':choice_a.description,
            'choice_b_description':choice_b.description,
        }
    else:
        context={
            'stage_description':stage.description,
            'choice_a_description':"",
            'choice_b_description':"",
        }
    return render(request, 'core/stage.html', context=context)


def stage_b(request):
    player = Player.objects.get(user=request.user)
    game = Game.objects.get(player=player)
    stage = game.stage
    
    next_stage = Stage.objects.get(id=game.stage.stage_b.id)
    game.stage = next_stage
    game.save()

    if next_stage.end_stage == False:
        choice_a = Choice.objects.get(stage=stage,choice_a=True)
        choice_b = Choice.objects.get(stage=stage,choice_b=True)
        
        context={
            'stage_description':stage.description,
            'choice_a_description':choice_a.description,
            'choice_b_description':choice_b.description,
        }
    else:
        context={
            'stage_description':stage.description,
            'choice_a_description':"",
            'choice_b_description':"",
        }
    return render(request, 'core/stage.html', context=context)

def end_game(request):
    player = Player.objects.get(user=request.user)
    player.game_number += 1
    player.save()

    stage = Stage.objects.get(root=True)
    game = Game.objects.create(player=player,stage=stage,end=False,game_number=player.game_number)
    game.save()

    return game

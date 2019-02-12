from django.conf import settings
from django import forms
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=400)
    game_number = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.email

class Game(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    stage = models.ForeignKey('Stage',on_delete=models.CASCADE, blank=True)
    end = models.BooleanField(default=False)
    game_number = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return str(self.game_number) + " - "+ self.player.email + " - "+ self.stage.description  

class Stage(models.Model):    
    description = models.CharField(max_length=400)
    root = models.BooleanField(default=False)

    a_stage = models.ForeignKey('self', on_delete=models.CASCADE, related_name='stage_a', blank=True)
    b_stage = models.ForeignKey('self', on_delete=models.CASCADE, related_name='stage_b', blank=True)

    end_stage = models.BooleanField(default=False)

    def __str__(self):
        return self.description

class Choice(models.Model):
    description = models.CharField(max_length=200)
    stage = models.ForeignKey(Stage,on_delete=models.CASCADE)
    choice_a = models.BooleanField(default=False)
    choice_b = models.BooleanField(default=False)
    
    def __str__(self):
        return self.description

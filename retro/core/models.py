from django.conf import settings
from django import forms
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=400)

    def __str__(self):
        return self.player.email

class Game(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    stage = models.ManyToManyField('Stage', blank=True)
    end = models.BooleanField(default=False)

    def __str__(self):
        return self.player.email

class Stage(models.Model):
    description = models.CharField(max_length=400)
    choices = models.ManyToManyField('Choice', blank=True)

class Choice(models.Model):
    description = models.CharField(max_length=200)

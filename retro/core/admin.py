from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

@admin.register(Game)
class Game(admin.ModelAdmin):
    pass

@admin.register(Player)
class Player(admin.ModelAdmin):
    pass

@admin.register(Stage)
class Stage(admin.ModelAdmin):
    pass

@admin.register(Choice)
class Choice(admin.ModelAdmin):
    pass
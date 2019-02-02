from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

@admin.register(Game)
class Game(admin.ModelAdmin):
    pass
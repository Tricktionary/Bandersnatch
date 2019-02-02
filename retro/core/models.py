from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Game(models.Model):
    score = models.IntegerField(blank=True, default=0)

    def increaseScore(self,score):
        self.score += score
        self.save()

    def __str__(self):
        return str(self.id)

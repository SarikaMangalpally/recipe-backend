import json
from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    servings = models.PositiveIntegerField(default=1)
    instructions = models.TextField()

    # def __str__(self):
    #     return self.title

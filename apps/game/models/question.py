from django.db import models
from apps.game.models.category import Category


class Question(models.Model):
    question = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/')


from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    imagem = models.CharField(max_length=300)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title


# myapp/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.username


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} ({self.points} points)"


class Reward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    points_required = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} ({self.points_required} points)"

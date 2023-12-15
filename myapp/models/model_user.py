# myapp/models/model_user.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.username
    
    class Meta:
        app_label = 'myapp'

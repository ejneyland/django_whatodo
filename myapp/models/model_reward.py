# myapp/models/model_reward
from django.db import models
from .model_user import User

class Reward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    points_required = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} ({self.points_required} points)"

    class Meta:
        app_label = 'myapp'
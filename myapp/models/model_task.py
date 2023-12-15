# myapp/models/model_task
from django.db import models
from .model_user import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField(auto_now_add=True)
    targ_comp_date = models.DateTimeField()
    description = models.TextField()
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} ({self.points} points)"
    
    class Meta:
        app_label = 'myapp'

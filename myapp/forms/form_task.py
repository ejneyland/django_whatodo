# your_app/forms.py
from django import forms
from ..models.model_task import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["user", "title", "targ_comp_date", "description", "points"]

        # You might want to customize the widgets, labels, etc., as needed
        widgets = {
            "targ_comp_date": forms.DateInput(attrs={"type": "date"}),
        }

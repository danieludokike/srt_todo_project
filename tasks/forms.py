from django import forms
from .models import Task 


class TaskForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter task title"
        })
    )
    
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter task description (optional)",
                "rows": 3
            }
        )
    )
    
    class Meta:
        model = Task
        fields = ["title", "description", "completed"]
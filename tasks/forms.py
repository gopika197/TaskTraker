from django import forms
from .models import Task

class TaskToggleForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['completed']
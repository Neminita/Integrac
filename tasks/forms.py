from django.forms import ModelForm
from .models import Task, Product

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']


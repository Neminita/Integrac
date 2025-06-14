from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    tittle = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add = True)
    detecompleted = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
    return self.title + '- by ' + self.user.username
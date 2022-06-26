from django.db import models
import datetime
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length= 512)
    created_at = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

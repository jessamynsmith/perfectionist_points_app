from django.db import models
from django.conf import settings


class TaskType(models.Model):
    name = models.CharField(max_length=40)
    points_available = models.IntegerField()


class Task(models.Model):
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    description = models.TextField()
    due_date = models.DateField
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

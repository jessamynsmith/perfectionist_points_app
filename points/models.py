from django.db import models
from django.conf import settings


class TaskType(models.Model):
    name = models.CharField(max_length=40)
    points_available = models.IntegerField()

    def __str__(self):
        return '{} - {} points'.format(self.name, self.points_available)


class Task(models.Model):
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    description = models.TextField()
    due_date = models.DateField()
    completed_date = models.DateField(null=True, blank=True)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    STATUS_LOOKUP = {
        False: 'Incomplete',
        True: 'Done!'
    }

    def __str__(self):
        return '{} ({})'.format(self.name, self.due_date)

    def is_complete(self):
        complete = False
        if self.completed_date:
            complete = True
        return complete

    def status(self):
        return self.STATUS_LOOKUP[self.is_complete()]

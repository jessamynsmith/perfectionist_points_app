from django.contrib import admin

from points import models


admin.site.register(models.Task)
admin.site.register(models.TaskType)

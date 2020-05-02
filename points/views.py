from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from points import models as points_models


class TaskListView(LoginRequiredMixin, ListView):

    model = points_models.Task

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(assigned_to=self.request.user)
        return queryset

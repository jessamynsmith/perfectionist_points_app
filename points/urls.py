
from django.urls import path
from points import views as points_views

urlpatterns = [
    path('', points_views.TaskListView.as_view(), name='task_list'),
]

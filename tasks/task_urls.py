from django.urls import path
from .views import TaskListView,TaskToggleView

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/toggle/<int:pk>/', TaskToggleView.as_view(), name='toggle_task'),
]

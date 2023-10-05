from django.shortcuts import render, redirect,get_object_or_404
from django.views import View
from .models import Task
from .forms import TaskToggleForm

class TaskListView(View):
    template_name = 'task/task_list.html'

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        return render(request, self.template_name, {'tasks': tasks})

class TaskToggleView(View):
    def post(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        if task.completed :
            completed_status= not task.completed
        else:
            completed_status = True
        form = TaskToggleForm(instance=task, data=request.POST)
        if form.is_valid():
            task.completed = completed_status
            task.save()
        else:
            print(f"Form Errors: {form.errors}")
        
        return redirect('task_list')
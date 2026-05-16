from django.views.generic import ListView, DeleteView
from .models import Task
# Create your views here.

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'

class TaskDetailView(DeleteView):
    model = Task
    template_name = 'task_detail.html'
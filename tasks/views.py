from asyncio import Task
from django.shortcuts import redirect, render
from django.views.generic import ListView,CreateView, UpdateView,DeleteView
from .models import TaskItem
from .forms import TaskItemCreateForm,TaskItemUpdateForm

# Create your views here.

class TodoItemListView(ListView):
    model = TaskItem
    template_name = 'tasks/todoitem_list.html'

class TodoItemCreateView(CreateView):
    model  = TaskItem
    template_name ='tasks/todoitem_create_form.html'
    form_class  =TaskItemCreateForm
    success_url = '/todo/list'


class TodoItemUpdateView(UpdateView):
    model  = TaskItem
    template_name ='tasks/todoitem_update_form.html'
    form_class  =TaskItemUpdateForm
    success_url = '/todo/list'


class TodoItemDeleteView(DeleteView):
    model = TaskItem
    template_name = 'tasks/todoitem_delete_form.html'
    success_url = "/owner/list"
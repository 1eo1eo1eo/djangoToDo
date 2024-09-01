from typing import TYPE_CHECKING

from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
)

from .models import ToDoItem

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse


class ToDoListIndexView(ListView):
    template_name = "todo_list/index.html"
    queryset = ToDoItem.objects.all()[:2]


class ToDoListView(ListView):
    model = ToDoItem


class ToDoListDoneView(ListView):
    queryset = ToDoItem.objects.filter(done=True).all()[:5]


class ToDoListNotDoneView(ListView):
    queryset = ToDoItem.objects.filter(done=False).all()[:5]


class ToDoDetailView(DetailView):
    model = ToDoItem

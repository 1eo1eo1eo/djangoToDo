from django.urls import path

from . import views


app_name = "todo_list"


urlpatterns = [
    path("", views.ToDoListIndexView.as_view(), name="index"),
    path("list/", views.ToDoListView.as_view(), name="list"),
    path("done/", views.ToDoListDoneView.as_view(), name="done"),
    path("notdone/", views.ToDoListNotDoneView.as_view(), name="notdone"),
    path("notdone/", views.ToDoListNotDoneView.as_view(), name="notdone"),
    path("detail/<int:pk>/", views.ToDoDetailView.as_view(), name="detail"),
]

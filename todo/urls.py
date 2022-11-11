from django.urls import path
from .views import *

app_name = "todo"

urlpatterns = [
    path("", home_view, name='home'),
    path("homepage/", homepage_view, name='homepage'),
    path("create/", createtodo_view, name="createtodo"),
    path("completed/", completedtodos_view, name="completetodo"),
    path("todo/<int:pk>", viewtodo, name="viewtodo"),
    path("todo/<int:pk>/complete", completetodo, name="completetodo"),
    path("todo/<int:pk>/delete", deletetodo, name="deletetodo")
]

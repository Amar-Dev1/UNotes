from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("home", views.home, name="home"),
    path("notes", views.home, name="notes"),
    path("create_note/", views.create_note, name="create_note"),
    path("notes/<int:id>", views.read_note, name="read_note"),
    path("notes/<int:id>/delete/", views.delete_note, name="delete_note"),
    path("note/<int:id>/update/", views.update_note, name="update_note"),
]

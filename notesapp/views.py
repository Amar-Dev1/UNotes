from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


# Create your views here.
def home(request):
    notes = Note.objects.all()
    context = {"title": "Home", "notes": notes}
    return render(request, "home.html", context)


def create_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = NoteForm()
    context = {"form": form, "title": "create note"}
    return render(request, "create_note.html", context)


def read_note(request, id):
    note = get_object_or_404(Note, id=id)
    context = {"note": note, "title": "read note"}
    return render(request, "read_note.html", context)


def delete_note(request, id):
    note = get_object_or_404(Note, id=id)
    if request.method == "POST":
        note.delete()
        return redirect("home")
    context = {"note": note}
    return render(request, "delete_note.html", context)


def update_note(request, id):
    note = get_object_or_404(Note, id=id)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        form.save()
        return redirect("home")
    else:
        form = NoteForm(instance=note)
    context = {"note": note, "form": form, "title": "update form"}
    return render(request, "update_note.html", context)

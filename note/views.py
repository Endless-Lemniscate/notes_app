from django.shortcuts import render
from .models import Note
from django.http import HttpResponse


def index(request):
    notes = Note.objects.all()
    return HttpResponse(f"hello {notes[0].title}")

from django.shortcuts import render
from django.http import JsonResponse
from notes_app.models import Note



# Create your views here.

def notes(request):

    notes_ = Note.objects.all()

    return JsonResponse([
        {   'url': f'api/note/{note.id}',
            'name': note.title,
            'content': note.content
        }
        for note in notes_
    ], safe = False)


def note(request, id):
    note_to_be_displayed = Note.objects.get(id = id)

    return JsonResponse({
        'name': note_to_be_displayed.title,
        'content': note_to_be_displayed.content
    })





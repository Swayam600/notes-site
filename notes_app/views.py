from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Note

# Create your views here.

def home(request):

	notes = Note.objects.all()

	return render(request, 'home.html', {'notes': notes})


def note(request, id):
	note = Note.objects.get(id = id)

	return render(request, 'note.html', {'note': note})

def add_note(request):

	if request.method == 'POST':
		new_note = Note(title = request.POST['title'], content = request.POST['content'])

		new_note.save()

		return redirect('/')

	return render(request, 'modify+note.html')

def modify(request, id):
	note_ = Note.objects.get(id = id)

	if request.method == 'POST':
		
		note_.title = request.POST['title']
		note_.content = request.POST['content']

		note_.save()

		return redirect('/')

	return render(request, 'modify+note.html', {'note': note_})

def delete_note(request, id):
	note_ = Note.objects.get(id = id)

	if request.method == 'POST':
		note_to_be_deleted = Note.objects.get(id = note_.id)
		note_to_be_deleted.delete()
		return redirect('/')

	return render(request, 'delete.html', {'note': note_})

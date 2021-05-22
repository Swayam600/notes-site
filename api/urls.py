from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.notes, name = 'notes-api'),
    path('note/<int:id>', views.note, name = 'note-api')
]





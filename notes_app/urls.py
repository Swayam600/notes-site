from django.urls import path
from . import views as v

urlpatterns = [
	path('', v.home, name = 'home-page'),
	path('note/<int:id>/', v.note, name = 'note-page'),
	path('add/', v.add_note, name = 'add-page'),
	path('modify/<int:id>', v.modify, name = 'modify-page'),
	path('delete/<int:id>', v.delete_note, name = 'delete-page')	
]
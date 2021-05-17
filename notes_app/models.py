from django.db import models

# Create your models here.

class Note(models.Model):
	title = models.CharField(max_length = 30, default = 'untitled')
	content = models.TextField(null = False)


	def __str__(self):
		return self.title
	
	def small(self):
		return self.content[:190]

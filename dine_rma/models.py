from django.db import models

# Create your models here.
class List(models.Model):
	name = models.CharField(max_length = 200)
	location = models.CharField(max_length = 200)
	intro = models.CharField(max_length = 500)

	def __str__(self):
		return str(self.name) +" | "+str(self.location)
from django.db import models

# Create your models here.

class hotel(models.Model):
	nombre = models.CharField(max_length=30)
	lugar = models.CharField(max_length=35)
	direccion = models.TextField()
	telefono = models.CharField(max_length=9)
	fecha = models.DateTimeField()

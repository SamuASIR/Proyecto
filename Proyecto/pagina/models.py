from django.db import models

# Create your models here.

class hotel(models.Model):
	nombre = models.CharField(max_length=50)
	lugar = models.CharField(max_length=35)
	direccion = models.TextField()
	telefono = models.CharField(max_length=9)
	web = models.URLField(max_length=100,null=True)

	def __str__(self):
		return '%s' % (self.nombre)

class reserva(models.Model):
	fecha_entrada = models.DateTimeField()
	fecha_salida = models.DateTimeField()
	n_habitacion = models.CharField(max_length=50)
	id_reserva = models.CharField(max_length=50)

	def __str__(self):
		return '%s' % (self.nombre)

class actividades(models.Model):
	spa = models.CharField(max_length=10)
	desayuno = models.CharField(max_length=10)
	comida = models.CharField(max_length=10)
	cena = models.CharField(max_length=10)

	def __str__(self):
		return '%s' % (self.nombre)

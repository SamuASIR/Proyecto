from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class hotel(models.Model):
	nombre = models.CharField(max_length=50)
	lugar = models.CharField(max_length=35)
	direccion = models.TextField()
	telefono = models.CharField(max_length=9)
	web = models.URLField(max_length=100,null=True)
	foto = models.ImageField(upload_to='pagina/static/media',null=True)

	def __str__(self):
		return '%s' % (self.nombre)

class reserva(models.Model):
	fecha_entrada = models.DateTimeField()
	fecha_salida = models.DateTimeField()
	hotel = models.ForeignKey(hotel,default=1)
	User =  models.ForeignKey(User, default=1)

	def __str__(self):
		return '%s' % (self.nombre)

class actividades(models.Model):
	spa = models.CharField(max_length=10)
	desayuno = models.CharField(max_length=10)
	comida = models.CharField(max_length=10)
	cena = models.CharField(max_length=10)

	def __str__(self):
		return '%s' % (self.nombre)

class usuario(models.Model):
	user = models.OneToOneField(User)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	direccion = models.CharField(max_length=50)
	telefono = models.CharField(max_length=50)
	mail = models.CharField(max_length=50)

	def __str__(self):
		return '%s' % (self.nombre)

class comentario(models.Model):
	usuario = models.ForeignKey(User)
	opinion = models.TextField()

	def __str__(self):
		return '%s' % (self.nombre)


	

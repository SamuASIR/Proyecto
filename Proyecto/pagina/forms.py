from django import forms
from pagina.models import reserva,comentario

class hotelForm(forms.ModelForm):

	class Meta:
		model = reserva
		fields = ('fecha_entrada','fecha_salida',)

class comentarioForm(forms.ModelForm):

	class Meta:
		model = comentario
		fields = ('opinion',)

from django import forms
from pagina.models import reserva

class hotelForm(forms.ModelForm):

	class Meta:
		model = reserva
		fields = ('fecha_entrada','fecha_salida',)

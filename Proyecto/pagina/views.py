from django.shortcuts import render
from pagina.models import hotel

# Create your views here.

def indice(request):
   portada = hotel.objects.all()
   return render(request, 'pagina/index.html', {'portada': portada })



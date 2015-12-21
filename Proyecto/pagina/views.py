from django.shortcuts import render,get_object_or_404
from pagina.models import hotel,reserva,comentario
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from pagina.forms import hotelForm,comentarioForm

# Create your views here.

# def Hace referencia a un html

def indice(request):
	portada = hotel.objects.all()
	return render(request, 'pagina/index.html', {'portada': portada })

def registro(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/")
	else:
		form = UserCreationForm()
	return render(request, "pagina/registro.html", {
'form': form,})

def loginpage(request):
	if request.method == 'POST':
		form = AuthenticationForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			return HttpResponseRedirect("/")
	else:
		form = AuthenticationForm()
	return render(request,'pagina/login.html', {'form': form,})  

def logoutpage(request):
	logout(request)
	return HttpResponseRedirect("/")

@login_required
def reservahotel(request,hotel_id):
	if request.method == "POST":
		form = hotelForm(request.POST, request.FILES)
		if form.is_valid():
			reserva = form.save()
			reserva.User = request.user
			reserva.hotel = get_object_or_404(hotel, pk = hotel_id)			
			reserva.save()
			return HttpResponseRedirect("/reserva_realizada")
	else:

		form = hotelForm()
	return render(request, 'pagina/reserva_hotel.html', {'form': form})

def reserva_realizada(request):
	portada = hotel.objects.all()
	return render(request, 'pagina/reserva_realizada.html', {'portada': portada })

@login_required
def mis_reservas(request):
	listareservas = reserva.objects.filter(User = request.user) #Funciona como un where
	return render(request, 'pagina/mis_reserva.html', {'listareservas': listareservas })

@login_required
def detalles(request,hotel_id):
	print(request.user)
	if request.method == "POST":
		form = comentarioForm(request.POST)
		if form.is_valid():
			comentarios = form.save()
			comentarios.usuario = request.user
			comentarios.hotel = get_object_or_404(hotel, pk = hotel_id)			
			comentarios.save()
			return HttpResponseRedirect("/detalles/"+hotel_id)
	else:
		form = comentarioForm()
		lista_comentarios = comentario.objects.filter(hotel=hotel_id)
		detalles_hotel = get_object_or_404(hotel, pk = hotel_id) #Esto es una variable "hotel"
	return render(request, 'pagina/detalles.html', {'detalles_hotel': detalles_hotel,'form':form,'lista_comentarios':lista_comentarios, }) #variable que pasas al html
	

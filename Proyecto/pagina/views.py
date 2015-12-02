from django.shortcuts import render
from pagina.models import hotel
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from pagina.forms import hotelForm

# Create your views here.

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
def reservahotel(request):
	if request.method == "POST":
		form = hotelForm(request.POST, request.FILES)
		if form.is_valid():
			receta = form.save()
			receta.save()
			return HttpResponseRedirect("/")
	else:
		form = hotelForm()
	return render(request, 'pagina/reserva_hotel.html', {'form': form})

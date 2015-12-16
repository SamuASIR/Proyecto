from django.conf.urls import url
from pagina import views

urlpatterns = [
   url(r'^$', views.indice, name='indice'),
	 url(r'^registro$', views.registro, name='registro'),
    url(r'^login$', views.loginpage, name='login'),
    url(r'^logout$', views.logoutpage, name='logout'),
	 url(r'^reservahotel/(?P<hotel_id>\d+)/$', views.reservahotel, name='reservahotel'),
	 url(r'^reserva_realizada$', views.reserva_realizada, name='reserva_realizada'),
	 url(r'^mis_reservas$', views.mis_reservas, name='mis_reservas'),
]

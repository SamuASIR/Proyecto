from django.conf.urls import url
from pagina import views

urlpatterns = [
   url(r'^$', views.indice, name='indice'),
]

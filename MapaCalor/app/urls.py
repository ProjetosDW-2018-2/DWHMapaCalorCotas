from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^filtro_mapa/', filtro_mapa, name='filtro_mapa')
]
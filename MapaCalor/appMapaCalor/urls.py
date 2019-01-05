from django.conf.urls import url
from .views import *

urlPatterns = [
    url(r'^filtro_mapa/', filtro_mapa, name='filtro_mapa')
]
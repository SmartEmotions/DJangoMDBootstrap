from django.conf.urls import url
from django.shortcuts import render
from Inicio.views import *

urlpatterns = [url(r'^inicio/', inicio, name='inicio'),]

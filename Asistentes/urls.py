from django.conf.urls import url
from Asistentes.views import *

urlpatterns = [url(r'^newRegister/', saveRegister, name='save-register'),
               url(r'^registrame/', register, name='register'),
               url(r'^asistencia/', presential, name='presential'),
               url(r'^savePresential/', savePresential, name='save-presential'),
               url(r'^getPresentials/', getPresentials, name='get-presentials'),]

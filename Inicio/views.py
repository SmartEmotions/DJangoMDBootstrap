from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import pyjade
def inicio(request):
    '''
    En la pagina de inicio se planea colocar un solo
    contenido srolling, lo otro es segmentar la pagina
    en varias dependera de las recomendaciones
    Colocar colores alusivos a la cultura indigena
    Colocar imagenes que correspondan a la intención convocatoria
    '''
    return render(request, 'index.html')

def about(request):
    '''
    En la pagina de inicio se planea colocar un solo
    contenido srolling, lo otro es segmentar la pagina
    en varias dependera de las recomendaciones
    Colocar colores alusivos a la cultura indigena
    Colocar imagenes que correspondan a la intención convocatoria
    '''
    return render(request, 'about.jade', {})

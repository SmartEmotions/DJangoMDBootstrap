from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from Asistentes.models import Registrados, Asistencia
import datetime, time, json

def saveRegister(request):
    if request.method == 'POST':
        name = (request.POST['name'] + ' ' + request.POST['lastname']).title()
        email = request.POST['email']
        code = request.POST['code']
        exist = Registrados.objects.filter(reg_code__contains=code
                                           ).filter(reg_email__icontains=email)
        if not exist:
            newRegister = Registrados(reg_nombre = name,
                                      reg_email = email,
                                      reg_code = code)
            newRegister.save()
            return HttpResponse(0)
        return HttpResponse(1)
    return HttpResponse(2)


def savePresential(request):
    if request.method == 'POST':
        code = request.POST['code']
        exist = Registrados.objects.filter(reg_code__contains=code)
        if exist:
            if registerHoursAgo(code) == 0:
                registrado = Registrados(reg_code = code)
                newPresential = Asistencia(reg_code = registrado)
                newPresential.save()
                return HttpResponse(0)
            return HttpResponse(1)
        return HttpResponse(2)
    return HttpResponse(3)

def register(request):
    '''
    En la pagina de inicio se planea colocar un solo
    contenido srolling, lo otro es segmentar la pagina
    en varias dependera de las recomendaciones
    Colocar colores alusivos a la cultura indigena
    Colocar imagenes que correspondan a la intención convocatoria
    '''
    return render(request, 'register.html')

def presential(request):
    '''
    En la pagina de inicio se planea colocar un solo
    contenido srolling, lo otro es segmentar la pagina
    en varias dependera de las recomendaciones
    Colocar colores alusivos a la cultura indigena
    Colocar imagenes que correspondan a la intención convocatoria
    '''
    return render(request, 'asistencia.html')


def registerHoursAgo(code):
    registrado = Registrados(reg_code=code)
    oneHourAgo = str(datetime.datetime.now() - datetime.timedelta(hours=4))
    register = Asistencia.objects.filter(reg_code=registrado, reg_date__gt=oneHourAgo)
    return len(register)

def getPresentials(request):
    asistentes = Asistencia.objects.extra(select={'day': 'date( reg_date )'}
                                         ).values('day').annotate(available=Count('reg_date')).order_by('day')
    response = []
    for asistente in asistentes:
        # asistente['day']=asistente['day'].strftime("%A %d %B %Y")
        asistente['day']=asistente['day'].strftime("%d %B")
        response.append(asistente)
    return HttpResponse(json.dumps(response))

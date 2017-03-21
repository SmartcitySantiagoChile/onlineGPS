from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View


# model
from gpsmap.models import UltimosGps, BusesDiarios

# Create your views here.
class MapHandler(View):
    '''This class manages the map where the markers from the devices using the
    application are shown'''

    def __init__(self):
        """the contructor, context are the parameter given to the html template"""
	self.context={}

    def get(self, request):
        template = "map.html"

	return render(request, template, self.context)

class GetMapPositions(View):
    '''This class requests to the database the values of the actives users'''

    def __init__(self):
        """the contructor, context are the parameter given to the html template"""
	self.context={}

    def get(self, request):

	# the position of interest are the ones ocurred in the last 10 minutes
	positions = UltimosGps.objects.all()
	#positions = UltimaCargaGps.objects.all()[:10]

	response = []
	for aPosition in positions:
	    response.append({'patente': aPosition.patente, 
                             'servicioCodigo': aPosition.servicio, 
                	     'servicio': aPosition.servicio_usuario, 
                	     'distEnRuta': aPosition.dist_en_ruta, 
                	     'distARuta': aPosition.dist_a_ruta, 
                	     'velocidadInstantanea': aPosition.velocidad_instantanea, 
                	     'velocidad2GPS': aPosition.velocidad_2gps, 
                	     'velocidad4GPS': aPosition.velocidad_4gps, 
                	     'operador': aPosition.operador, 
                	     'latitud': aPosition.latitud, 
                	     'longitud': aPosition.longitud, 
                	     'tiempo': aPosition.tiempo,
                	     'orientacion': aPosition.orientacion,
                	     'tipo': aPosition.tipo,
                	     'capacidad': aPosition.capacidad})
	    #response.append({'patente': aPosition.patente, 'servicio': aPosition.servicio, 'latitud': aPosition.latitud, 'longitud': aPosition.longitud, 'tiempo': aPosition.tiempo})
	return JsonResponse(response, safe=False)

class GetMapPositionsByService(View):
    '''This class requests to the database the values of the actives users'''

    def __init__(self):
        """the contructor, context are the parameter given to the html template"""
	self.context={}

    def get(self, request, service, direction):
	# the position of interest are the ones ocurred in the last 10 minutes
	positions = UltimosGps.objects.filter(servicio_usuario__iregex=r'{0}{1}$'.format(service, direction))

	response = []
	for aPosition in positions:
		noStop = BusesDiarios.objects.filter(patente=aPosition.patente).order_by('-t_inicial').first()
		noStopNum = "No Info."
		if noStop is not None:
			noStopNum = noStop.no_detenciones
        	response.append({'patente': aPosition.patente, 
                	'servicioCodigo': aPosition.servicio, 
                	'servicio': aPosition.servicio_usuario, 
                	'distEnRuta': aPosition.dist_en_ruta, 
                	'distARuta': aPosition.dist_a_ruta, 
                	'velocidadInstantanea': aPosition.velocidad_instantanea, 
                	'velocidad2GPS': aPosition.velocidad_2gps, 
                	'velocidad4GPS': aPosition.velocidad_4gps, 
                	'operador': aPosition.operador, 
                	'latitud': aPosition.latitud, 
                	'longitud': aPosition.longitud, 
                	'tiempo': aPosition.tiempo,
                	'orientacion': aPosition.orientacion,
                	'tipo': aPosition.tipo,
                	'capacidad': aPosition.capacidad,
                	'noParo': noStopNum})
	return JsonResponse(response, safe=False)

class ServiceHandler(View):
    '''This class manages the map where the markers from the devices using the
    application are shown'''

    def __init__(self):
        """the contructor, context are the parameter given to the html template"""
	self.context={}

    def get(self, request):
        template = "service.html"

	return render(request, template, self.context)



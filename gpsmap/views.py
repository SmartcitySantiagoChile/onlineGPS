from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View


# model
from gpsmap.models import UltimosGps, UltimaCargaGps

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
	    response.append({'patente': aPosition.patente, 'servicio': aPosition.servicio, 'fuera_de_ruta': aPosition.fuera_de_ruta, 'latitud': aPosition.latitud, 'longitud': aPosition.longitud, 'tiempo': aPosition.tiempo})
	    #response.append({'patente': aPosition.patente, 'servicio': aPosition.servicio, 'latitud': aPosition.latitud, 'longitud': aPosition.longitud, 'tiempo': aPosition.tiempo})
	return JsonResponse(response, safe=False)

class GetMapPositionsByService(View):
    '''This class requests to the database the values of the actives users'''

    def __init__(self):
        """the contructor, context are the parameter given to the html template"""
	self.context={}

    def get(self, request, service, direction):
	# the position of interest are the ones ocurred in the last 10 minutes
	positions = UltimosGps.objects.filter(servicio__iregex=r'.*{0}.*{1}$'.format(service, direction))
	#positions = UltimaCargaGps.objects.all()[:10]

	response = []
	for aPosition in positions:
	    response.append({'patente': aPosition.patente, 
                'servicio': aPosition.servicio, 
                'fuera_de_ruta': aPosition.fuera_de_ruta, 
                'latitud': aPosition.latitud, 
                'longitud': aPosition.longitud, 
                'tiempo': aPosition.tiempo})
	    #response.append({'patente': aPosition.patente, 'servicio': aPosition.servicio, 'latitud': aPosition.latitud, 'longitud': aPosition.longitud, 'tiempo': aPosition.tiempo})
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



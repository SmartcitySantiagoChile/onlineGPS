from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

# model
from timepredictor.models import PrediccionTiempos, UltimosGps

# Create your views here.
class MapHandler(View):
    '''This class manages the map where the bus and stops are shown'''

    def __init__(self):
	self.context={}

    def get(self, request):
        template = "timePredictor.html"

	return render(request, template, self.context)

class GetEstimatedTimes(View):
    '''This class requests to the database the estimated times for next stops for a bus'''

    def __init__(self):
	self.context={}

    def get(self, request, licencePlate):

	# the position of interest are the ones ocurred in the last 10 minutes
	stops = PrediccionTiempos.objects.filter(patente = licencePlate).order_by('-tiempo_tstamp')
	#positions = UltimaCargaGps.objects.all()[:10]

	response = {}
        busDesc = 'bus'
        stopsDesc = 'stops'
	response[stopsDesc] = []
	for stop in stops:
            if not busDesc in response:
                response[busDesc] = {
                    'licencePlate': stop.patente, 
                    'AuthRoute': stop.servicio
                }
	    response[stopsDesc].append(
                    {'stopCode': stop.codigo, 
                     'arrivedEstimatedTime': stop.tiempo_tstamp, 
                     'distanceOnRoute': stop.distancia, 
                     'arrivedEstimatedTimeInSecs': stop.tiempo})

	return JsonResponse(response, safe=False)

class GetBusPosition(View):
    '''This class requests to the database the position of a bus '''

    def __init__(self):
        """the contructor, context are the parameter given to the html template"""
	self.context={}

    def get(self, request, licencePlate):
	# the position of interest are the ones ocurred in the last 10 minutes
        positions = UltimosGps.objects.filter(patente = licencePlate)

	response = []
	for aPosition in positions:
	    response.append({
                'licencePlate': aPosition.patente, 
                'authRoute': aPosition.servicio, 
                'userRoute': aPosition.servicio_usuario, 
                'distOnroute': aPosition.dist_en_ruta, 
                'distToRoute': aPosition.dist_a_ruta, 
                'InstVelocity': aPosition.velocidad_instantanea, 
                'velocity2GPS': aPosition.velocidad_2gps, 
                'velocity4GPS': aPosition.velocidad_4gps, 
                'operator': aPosition.operador, 
                'latitude': aPosition.latitud, 
                'longitude': aPosition.longitud, 
                'time': aPosition.tiempo,
                'orientation': aPosition.orientacion,
                'type': aPosition.tipo,
                'capacity': aPosition.capacidad})

	return JsonResponse(response, safe=False)

class GetActiveBuses(View):
    '''This class requests to the database the buses are doing a trip '''

    def __init__(self):
	self.context={}

    def get(self, request):
        activeBuses = UltimosGps.objects.order_by('patente', 'servicio').distinct('patente', 'servicio')

	response = []
	for activeBus in activeBuses:
	    response.append({
                'licencePlate': activeBus.patente, 
                'authRoute': activeBus.servicio, 
                'userRoute': activeBus.servicio_usuario, 
                #'distOnroute': activeBus.dist_en_ruta, 
                #'distToRoute': activeBus.dist_a_ruta, 
                #'InstVelocity': activeBus.velocidad_instantanea, 
                #'velocity2GPS': activeBus.velocidad_2gps, 
                #'velocity4GPS': activeBus.velocidad_4gps, 
                #'operator': activeBus.operador, 
                #'latitude': activeBus.latitud, 
                #'longitude': activeBus.longitud, 
                #'time': activeBus.tiempo,
                #'orientation': activeBus.orientacion,
                #'type': activeBus.tipo,
                #'capacity': activeBus.capacidad
                })

	return JsonResponse(response, safe=False)



from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.db import connection

from velocityperstreet.models import Tramos15Min, OrigenYDestinoEjes15Min

# Create your views here.
class GetStreetData(View):
    '''This class requests to the database the street secction with travel time '''

    def __init__(self):
        """the contructor, context are the parameter given to the html template"""
        self.context={}

    def get(self, request):
        """ the {quantity} bus stops with most waiting time for a bus """
        points = Tramos15Min.objects.all().order_by('eje', 'tramo', 'dist_en_ruta')

        dest = 'Destination'
        response = {}
        response[dest] = {}
        for point in points:
            if not point.destino in response[dest]:
                response[dest][point.destino] = {}
            if not point.zona in response[dest][point.destino]:
                response[dest][point.destino][point.zona] = {}
            if not point.eje in response[dest][point.destino][point.zona]:
                street = {}
                #street['name'] = point.eje
                street['origin'] = point.hito_origen
                street['destination'] = point.hito_destino
                #street['zone'] = point.zona
                #street['zoneGoal'] = point.destino
                street['time'] = point.tiempo_viaje_ultimo_15_eje
                street['velocity'] = point.velocidad_eje
                street['sections'] = {}
                response[dest][point.destino][point.zona][point.eje] = street
             
            if not point.tramo in response[dest][point.destino][point.zona][point.eje]['sections']:
                section = {}
                section['originStreet'] = point.calle_origen
                section['destinationStreet'] = point.calle_destino
                section['velocity'] = point.velocidad_ultimo_15_tramo
                section['time'] = point.tiempo_viaje_ultimo_15_tramo
                section['points'] = []
                response[dest][point.destino][point.zona][point.eje]['sections'][point.tramo] = section

            response[dest][point.destino][point.zona][point.eje]['sections'][point.tramo]['points'].append({
                'distOnRoute': point.dist_en_ruta, 
                'latitude': point.latitud, 
                'longitude': point.longitud})

        return JsonResponse(response, safe=False)

class GetPOIData(View):
    '''This class requests to the database the street limits '''

    def __init__(self):
        """the contructor, context are the parameter given to the html template"""
        self.context={}

    def get(self, request):
        """ the {quantity} bus stops with most waiting time for a bus """
        points = OrigenYDestinoEjes15Min.objects.all().order_by('eje')

        response = {}
        POIs = []
        for point in points:
            aux = {}
            aux['street'] = point.eje
            aux['origin'] = point.hito_origen
            aux['destination'] = point.hito_destino
            aux['zone'] = point.zona
            aux['zoneGoal'] = point.destino
            aux['name'] = point.nombre
            aux['latitude'] = point.latitud
            aux['longitude'] = point.longitud
            POIs.append(aux)
        response['POIs'] = POIs
 
        return JsonResponse(response, safe=False)


class StreetMapHandler(View):
    '''This class manages the map where the street section are shown'''

    def __init__(self):
        """the contructor, context are the parameter given to the html template"""
        self.context={}

    def get(self, request):
        template = "streets.html"

        return render(request, template, self.context)

class StreetVelocityMapHandler(View):
    '''This class manages the map where the street section are shown'''

    def __init__(self):
        """the contructor, context are the parameter given to the html template"""
        self.context={}

    def get(self, request):
        template = "streetsVelocity.html"

        return render(request, template, self.context)


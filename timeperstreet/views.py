from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.db import connection

from timeperstreet.models import Tramos15Min, OrigenYDestinoEjes15Min, EjesMacro, VelocidadGlobal

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
                street['time'] = point.tiempo_viaje_eje
                street['velocity'] = point.velocidad_eje
                street['sections'] = {}
                response[dest][point.destino][point.zona][point.eje] = street
             
            if not point.tramo in response[dest][point.destino][point.zona][point.eje]['sections']:
                section = {}
                section['originStreet'] = point.calle_origen
                section['destinationStreet'] = point.calle_destino
                section['velocity'] = point.velocidad_tramo
                section['time'] = point.tiempo_viaje_tramo
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

        dest = 'Destination'
        response = {}
        response[dest] = {}
        for point in points:
            if not point.destino in response[dest]:
                response[dest][point.destino] = {}
            if not point.zona in response[dest][point.destino]:
                response[dest][point.destino][point.zona] = {}
            if not point.eje in response[dest][point.destino][point.zona]:
                response[dest][point.destino][point.zona][point.eje] = []
            aux = {}
            aux = {}
            aux['origin'] = point.hito_origen
            aux['destination'] = point.hito_destino
            aux['name'] = point.nombre
            aux['latitude'] = point.latitud
            aux['longitude'] = point.longitud
            
            response[dest][point.destino][point.zona][point.eje].append(aux)
 
        return JsonResponse(response, safe=False)


class StreetTimeMapHandler(View):
    '''This class manages the map where the street section are shown'''

    def __init__(self):
        """the contructor, context are the parameter given to the html template"""
        self.context={}

    def get(self, request):
        template = "streetsTime.html"

        return render(request, template, self.context)


def getColor(velocity):
    """
    grey
    red
    orange
    yeloow
    green
    dark green
    blue
    """
    return '#c4c4c4' if velocity <  0  else \
           '#ff0000' if velocity <= 15 else \
           '#ff9000' if velocity <= 19 else \
           '#fff600' if velocity <= 21 else \
           '#19ff00' if velocity <= 25 else \
           '#0d8900' if velocity <= 30 else \
           '#2133f2'


class GetStreetTableData(View):
    '''This class requests to the database the street secction with travel time '''

    def __init__(self):
        """the contructor, context are the parameter given to the html template"""
        self.context={}

    def get(self, request):
        ''' '''
        axisId = request.GET.get('axisId')
        if axisId:
            points = Tramos15Min.objects.filter(eje_id=axisId)
        else:
            points = Tramos15Min.objects.all()
        points = points.values('eje', 'hito_origen', 'hito_destino', 'tiempo_viaje_eje', 'velocidad_eje').distinct()

        response = []
        for point in points:
            street = {}
            street['axis'] = point['eje']
            street['origin'] = point['hito_origen']
            street['destination'] = point['hito_destino']
            street['time'] = 'Sin datos' if point['tiempo_viaje_eje'] == -1 else int(point['tiempo_viaje_eje']/60)
            street['color'] = getColor(point['velocidad_eje'])

            response.append(street)

        return JsonResponse(response, safe=False)

class GetMacroStreetTableData(View):
    ''' This class requests to the database the macro streets data '''

    def __init__(self):
        """the contructor, context are the parameter given to the html template"""
        self.context={}

    def get(self, request):
        """ the {quantity} bus stops with most waiting time for a bus """
        
        response = []
        for point in EjesMacro.objects.all():
            street = {}
            street['axis'] = point.eje_id
            street['origin'] = point.hito_origen
            street['destination'] = point.hito_destino
            street['time'] = 'Sin datos' if point.tiempo_viaje == -1 else point.tiempo_viaje
            street['color'] = getColor(point.velocidad)

            response.append(street)

        return JsonResponse(response, safe=False)

class GetGlobalVelocity(View):
    ''' Get the global velocity of the transport system. It separates in two metrics: corridor and not corridor '''

    def __init__(self):
        """the contructor, context are the parameter given to the html template"""
        self.context={}

    def get(self, request):
        ''' '''
        avgVelocities = VelocidadGlobal.objects.first()

        response = {'corridor': avgVelocities['velocidad_con_corredor'], 
                    'notCorridor': avgVelocities['velocidad_sin_corredor']}
        return JsonResponse(response, safe=False)


class StreetTimeTableMapHandler(View):
    '''This class manages the map where the street section are shown as a table'''

    def __init__(self):
        """the contructor, context are the parameter given to the html template"""
        self.context={}

    def get(self, request):
        template = "timeTable.html"

        return render(request, template, self.context)


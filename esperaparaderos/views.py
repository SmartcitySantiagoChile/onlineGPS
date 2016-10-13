from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

from esperaparaderos.models import InfoParadas

from datetime import datetime

# Create your views here.
class GetWaitingUsersByBusStop(View):
    '''This class requests to the database the number of users are waiting for a bus by bus stop'''

    def __init__(self):
        """the contructor, context are the parameter given to the html template"""
        self.context={}

    def get(self, request, quantity):
        """ the {quantity} most populated bus stops """
        busStops = InfoParadas.objects.all().order_by('-subidas')[:quantity]

        return JsonResponse(applyFormatAnswer(busStops), safe=False)

class GetMostDelayedBusesByBusStop(View):
    '''This class requests to the database the bus stops with most waiting time by bus stop '''

    def __init__(self):
        """the contructor, context are the parameter given to the html template"""
        self.context={}

    def get(self, request, quantity):
        """ the {quantity} bus stops with most waiting time for a bus """
        busStops = InfoParadas.objects.all().order_by('tiempo_ultimo_bus')[:quantity]

        return JsonResponse(applyFormatAnswer(busStops), safe=False)

class WaitingUsersByBusStopMapHandler(View):
    '''This class manages the map where the bus stop with waiting users markers are shown'''

    def __init__(self):
        """the contructor, context are the parameter given to the html template"""
        self.context={}

    def get(self, request):
        template = "waitingUsersByBusStop.html"

        return render(request, template, self.context)

def applyFormatAnswer(busStops):
    response = []
    for busStop in busStops:
        now = datetime.now()
        timeDiff = now - busStop.tiempo_ultimo_bus
        seconds = timeDiff.total_seconds() 
        timeDiffF = str(timeDiff)
        response.append({'codigo': busStop.codigo,
            'latitud': busStop.latitud,
            'longitud': busStop.longitud,
            'tiempoUltimoBus': busStop.tiempo_ultimo_bus,
            'subidas': busStop.subidas,
            'segSinBus': seconds, 
            'tiempoSinBusF': timeDiffF})
    return response


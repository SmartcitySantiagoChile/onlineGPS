from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

# Create your views here.
from django.http import HttpResponse

from dailybusesinfo.models import BusesDiarios

class Info(View):
    '''This class manages the table where te data is shown'''

    def __init__(self):
        self.context={}

    def get(self, request):
        template = "dailyBusesInfo.html"

        return render(request, template, self.context)

class GetBusesInfo(View):
    '''This class requests to the database the info of the buses '''

    def __init__(self):
	self.context={}

    def isKnownRoute(self, code):
        if code == 0:
            return "Si"
        return "No"

    def isStationary(self, code):
        if code == 0:
            return "No"
        return "Si"

    def get(self, request):
        buses = BusesDiarios.objects.order_by('servicio', 'patente')

	data = []
	for bus in buses:
            data.append([
                bus.servicio,
                bus.patente,
                bus.t_inicial,
                bus.t_final, 
                bus.km_en_ruta, 
                bus.km_fuera_ruta,
                str(bus. t_en_ruta),
                str(bus.t_fuera_ruta),
                bus.velocidad_media,
                bus.costo_en_ruta, 
                bus.costo_fuera_ruta,
                bus.no_detenciones,
                self.isKnownRoute(bus.existe_ruta),
                self.isStationary(bus.tipo_expedicion), ])

	response = dict( [("data" , data)] )

	return JsonResponse(response, safe=False)

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

    def get(self, request):
        buses = BusesDiarios.objects.order_by('servicio', 'patente')

	data = []
	for bus in buses:
            data.append([
                bus.servicio,
                bus.patente, 
                bus.km_en_ruta, 
                bus.km_fuera_ruta, 
                bus.costo_en_ruta, 
                bus.costo_fuera_ruta, ])

	response = dict( [("data" , data)] )

	return JsonResponse(response, safe=False)

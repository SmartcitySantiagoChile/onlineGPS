# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.db import connection
from django.conf import settings

# Create your views here.

from speedbyroute.models import Tramos15minAll

class GetInfoRouteData(View):

	def __init__(self):
		self.context={}
	
	def get(self, request, routeName):
		
		points = Tramos15minAll.objects.filter(servicio_usuario=routeName).order_by('tramo')

		response = {}
		response['error'] = False
		try:
                        id=0
                        response['route'] = {}
                        response['route']['name'] = routeName
                        response['route']['sections'] = {}
			for point in points:
                            if not point.tramo in response['route']['sections']:
                                section = {}
                                section['speed'] = point.velocidad
                                section['travel_time'] = point.tiempo_viaje
                                section['points'] = []
                                response['route']['sections'][point.tramo] = section

                            response['route']['sections'][point.tramo]['points'].append({'latitude': point.latitud,'longitude': point.longitud})

		except Exception as e:
			response['error'] = True
			response['message'] = str(e)
			response['route'] = {}

		return JsonResponse(response,safe=False)
		
	
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
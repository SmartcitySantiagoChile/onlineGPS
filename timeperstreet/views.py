from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.db import connection

from timeperstreet.models import  StreetSection15Min, VelocityOfLast15Min

# Create your views here.
class GetStreetData(View):
    '''This class requests to the database the street secction with travel time '''

    def __init__(self):
        """the contructor, context are the parameter given to the html template"""
        self.context={}

    def get(self, request):
        """ the {quantity} bus stops with most waiting time for a bus """
        points = StreetSection15Min.objects.all().order_by('eje', 'id', 'dist_en_ruta')

        response = {}
        """
        for point in points:
            if not point.eje in response:
                response[point.eje] = []
            #if not point.id in response[point.eje]:
            #    response[point.eje][point.id] = []

            #response[point.eje][point.id].append({
            response[point.eje].append({
                'distOnRoute': point.dist_en_ruta, 
                'velocity': 1, #point.velocity, 
                'latitude': point.latitud, 
                'longitude': point.longitud, 
                'section': point.id})
        """

        with connection.cursor() as cursor:
            cursor.execute("SELECT a.id, a.eje, a.dist_en_ruta, a.latitud, a.longitud, b.velocidad FROM tramos_15min AS a LEFT JOIN velocidad_ultima_15min AS b ON a.id = b.tramo AND a.eje = b.eje WHERE b.velocidad IS NOT NULL")
            for point in cursor.fetchall():
                if not point[1] in response:
                    response[point[1]] = []
                response[point[1]].append({
                    'distOnRoute': point[2], 
                    'velocity': point[5], 
                    'latitude': point[3], 
                    'longitude': point[4], 
                    'section': point[0]})

           

        return JsonResponse(response, safe=False)

class StreetMapHandler(View):
    '''This class manages the map where the street section are shown'''

    def __init__(self):
        """the contructor, context are the parameter given to the html template"""
        self.context={}

    def get(self, request):
        template = "streets.html"

        return render(request, template, self.context)


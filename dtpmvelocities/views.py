from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.db import connection

from dtpmvelocities.models import *

# Create your views here.
class MapHandler(View):
    '''This class manages the map where the street section are shown'''

    def __init__(self):
        self.context = {}

    def get(self, request):
        template = "dtpmVelocities.html"

        return render(request, template, self.context)


from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View


# model
from gpsmap.models import *

# Create your views here.
class IndexHandler(View):
    '''This class manages the map where the markers from the devices using the
    application are shown'''

    def __init__(self):
        """the contructor, context are the parameter given to the html template"""
	self.context={}

    def get(self, request):
        template = "index.html"

	return render(request, template, self.context)

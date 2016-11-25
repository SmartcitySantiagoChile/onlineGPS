from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View


# model
#from drawroute.models import *

# Create your views here.
class MapHandler(View):
    '''This class manages the map where lines are drawn '''

    def __init__(self):
	self.context={}

    def get(self, request):
        template = "drawroute.html"

	return render(request, template, self.context)



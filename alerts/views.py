from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.db import connection

import requests
import json
import os

# Create your views here.
class AlertTableHandler(View):
    ''' '''

    def __init__(self):
        """the contructor, context are the parameter given to the html template"""
        self.context={}

    def get(self, request):
        template = "alerts/alertsTable.html"

        return render(request, template, self.context)

class GetTableData(View):
    ''' '''

    def __init__(self):
        """the contructor, context are the parameter given to the html template"""
        self.context={}

    def get(self, request):
        ''' '''
        URL = 'http://www.dtpmetropolitano.cl/alertas'

        with open(os.path.join(os.path.dirname(__file__), 'auth.json')) as file:
            jsonDoc = json.load(file)
            user = jsonDoc['user']
            password = jsonDoc['password']
       
        response = requests.get(URL, auth=(user, password))

        jsonContent = json.loads(response.content)

        return JsonResponse(jsonContent['registros'], safe=False)


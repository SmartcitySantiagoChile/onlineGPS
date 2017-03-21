from django.test import TestCase, Client
from django.utils import timezone

# python stuf
import json
import os
import csv

# model
from timeperstreet.models import Tramos15Min, OrigenYDestinoEjes15Min
# views
from timeperstreet.views import GetStreetData, GetPOIData, StreetTimeMapHandler, GetStreetTableData, StreetTimeTableMapHandler

# Create your tests here.

class TimePerStreetTestCase(TestCase):
    """ test for views """
    URL_PREFIX = '/timePerStreet/'

    def makeGetRequest(self, url, params = {}):

        URL = TimePerStreetTestCase.URL_PREFIX + url
        c = Client()
        response = c.get(URL, params)
        self.assertEqual(response.status_code, 200)
        
        return response

    def makePostRequest(self, url, params = {}):

        URL = TimePerStreetTestCase.URL_PREFIX + url
        c = Client()
        response = c.post(URL, params)
        self.assertEqual(response.status_code, 200)

        return response

    def printJson(self, jsonResponse):

        print json.dumps(jsonResponse, 
                sort_keys=True, 
                indent=4, 
                separators=(',', ': '))
 
    def setUp(self):
        """ save initial data on database """
        self.dirPath = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(self.dirPath, 'testStreetData.csv')) as f:
            # skip first line
            f.readline()
            reader = csv.reader(f)
            for row in reader:
                _, created = Tramos15Min.objects.get_or_create(
                                 eje_id       =row[1],
                                 secuencia_eje_macro=row[2],
                                 tramo        =row[3],
                                 eje          =row[4],
                                 hito_origen  =row[5],
                                 hito_destino =row[6],
                                 zona         =row[7],
                                 destino      =row[8],
                                 calle_origen =row[9],
                                 calle_destino=row[10],
                                 dist_en_ruta =row[11],
                                 latitud      =row[12],
                                 longitud     =row[13],
                                 x            =row[14],
                                 y            =row[15],
                                 velocidad_tramo    =row[16],
                                 tiempo_viaje_tramo =row[17],
                                 tiempo_viaje_eje   =row[18],
                                 velocidad_eje      =row[19],
                                 super_lento        =row[20]
                                 )
        with open(os.path.join(self.dirPath,'testPOIData.csv')) as f:
            # skip first line
            f.readline()
            reader = csv.reader(f)
            for row in reader:
                _, created = OrigenYDestinoEjes15Min.objects.get_or_create(
                                 eje=row[1],
                                 hito_origen=row[2],
                                 hito_destino=row[3],
                                 zona=row[4],
                                 destino=row[5],
                                 nombre=row[6],
                                 latitud=row[7],
                                 longitud=row[8]
                )

    def testGetStreetTableData(self):

        url = 'getStreetTableData'
        response = self.makeGetRequest(url, {})
        jsonResponse = json.loads(response.content)
        
        with open(os.path.join(self.dirPath, 'getStreetTableDataResponse.json')) as f:
            expectedJson = json.load(f)
     
            #self.printJson(jsonResponse)
            self.assertEqual(len(jsonResponse), len(expectedJson))
            for row in jsonResponse:
                self.assertEqual(row['origin'], expectedJson[0]['origin'])
                self.assertEqual(row['color'], expectedJson[0]['color'])
                self.assertEqual(row['destination'], expectedJson[0]['destination'])
                self.assertEqual(row['time'], expectedJson[0]['time'])
                self.assertEqual(row['axis'], expectedJson[0]['axis'])

    def testPOIData(self):

        url = 'getPOIData'
        response = self.makeGetRequest(url, {})
        jsonResponse = json.loads(response.content)

        with open(os.path.join(self.dirPath, 'getPOIDataResponse.json')) as f:
            expectedJson = json.load(f)
            
            self.assertEqual(len(jsonResponse), len(expectedJson))

    def testGetStreetData(self):

        url = 'getStreetData'
        
        response = self.makeGetRequest(url, {})

        jsonResponse = json.loads(response.content)
        
        with open(os.path.join(self.dirPath, 'getStreetDataResponse.json')) as f:
            expectedJson = json.load(f)
            
            self.assertEqual(len(jsonResponse), len(expectedJson))

    def testGetColor(self):

        tableData = GetStreetTableData()

        self.assertEqual(tableData.getColor(-1), '#c4c4c4')
        self.assertEqual(tableData.getColor(15), '#ff0000')
        self.assertEqual(tableData.getColor(19), '#ff9000')
        self.assertEqual(tableData.getColor(21), '#fff600')
        self.assertEqual(tableData.getColor(25), '#19ff00')
        self.assertEqual(tableData.getColor(30), '#0d8900')
        self.assertEqual(tableData.getColor(45), '#2133f2')

    def testMapView(self):

        url = 'show'
        response = self.makeGetRequest(url)

    def testTableView(self):

        url = 'show2'
        response = self.makeGetRequest(url)



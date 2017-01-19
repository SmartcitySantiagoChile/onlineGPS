from django.test import TestCase, Client
from django.utils import timezone

# python stuf
import json

# model
from beacon.models import DetectorDevice, Beacon, BeaconLog, Event
# views
from beacon.views import GetBeaconsData, GetEventsData, SaveData, Plot

# Create your tests here.

class BeaconTestCase(TestCase):
    """ test for register report view """
    URL_PREFIX = '/beacon/'

    def makeGetRequest(self, url, params = {}):

        URL = BeaconTestCase.URL_PREFIX + url
        c = Client()
        response = c.get(URL, params)
        self.assertEqual(response.status_code, 200)
        
        return response

    def makePostRequest(self, url, params = {}):

        URL = BeaconTestCase.URL_PREFIX + url
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

        self.deviceId = "94c97a7f526ade72"
        jsonData1 = """{
        "DeviceID":"94c97a7f526ade72",
        "MeasureData":{
            "Beacons":[
             {"Mac Address":"[F7:BD:38:83:E5:83]",
              "UUID":"7eccfcfa-f334-4042-9dc2-5b5432c33e06",
              "Major":2,
              "Minor":1,
              "Log":[
                 {"Time":"2017-01-09 14:35:19","RSSI":-47,"Measure Power":-51},
                 {"Time":"2017-01-09 14:35:24","RSSI":-49,"Measure Power":-51},
                 {"Time":"2017-01-09 14:35:29","RSSI":-47,"Measure Power":-51},
                 {"Time":"2017-01-09 14:35:34","RSSI":-47,"Measure Power":-51},
                 {"Time":"2017-01-09 14:35:39","RSSI":-48,"Measure Power":-51},   
                 {"Time":"2017-01-09 14:35:44","RSSI":-49,"Measure Power":-51},   
                 {"Time":"2017-01-09 14:35:49","RSSI":-47,"Measure Power":-51},
                 {"Time":"2017-01-09 14:35:55","RSSI":-47,"Measure Power":-51},
                 {"Time":"2017-01-09 14:36:00","RSSI":-47,"Measure Power":-51},   
                 {"Time":"2017-01-09 14:36:05","RSSI":-48,"Measure Power":-51},
                 {"Time":"2017-01-09 14:36:10","RSSI":-47,"Measure Power":-51},
                 {"Time":"2017-01-09 14:36:15","RSSI":-46,"Measure Power":-51},
                 {"Time":"2017-01-09 14:36:20","RSSI":-47,"Measure Power":-51}
               ]
             },
             {"Mac Address":"[E0:F4:4F:F4:98:69]",
              "UUID":"7eccfcfa-f334-4042-9dc2-5b5432c33e06",
              "Major":1,
              "Minor":2,
              "Log":[
                 {"Time":"2017-01-09 14:36:19","RSSI":-77,"Measure Power":-51},
                 {"Time":"2017-01-09 14:36:24","RSSI":-73,"Measure Power":-51},
                 {"Time":"2017-01-09 14:36:29","RSSI":-69,"Measure Power":-51},
                 {"Time":"2017-01-09 14:36:34","RSSI":-70,"Measure Power":-51},
                 {"Time":"2017-01-09 14:36:39","RSSI":-69,"Measure Power":-51},
                 {"Time":"2017-01-09 14:36:44","RSSI":-69,"Measure Power":-51},
                 {"Time":"2017-01-09 14:36:49","RSSI":-70,"Measure Power":-51},
                 {"Time":"2017-01-09 14:36:55","RSSI":-67,"Measure Power":-51},
                 {"Time":"2017-01-09 14:37:00","RSSI":-68,"Measure Power":-51},
                 {"Time":"2017-01-09 14:37:05","RSSI":-68,"Measure Power":-51},
                 {"Time":"2017-01-09 14:37:10","RSSI":-68,"Measure Power":-51},
                 {"Time":"2017-01-09 14:37:15","RSSI":-67,"Measure Power":-51},
                 {"Time":"2017-01-09 14:37:20","RSSI":-70,"Measure Power":-51}
              ]
             }
            ],
            "Events":[
                {"Time":"2017-01-09 14:36:00","Event":"Esto es una prueba"},
                {"Time":"2017-01-09 14:36:05","Event":"Esto es otra prueba"}
            ]}
        }"""
 
        jsonData2 ="""{
        "DeviceID":"000000000000000",
        "MeasureData":{
            "Beacons":[
             {"Mac Address":"[F7:BD:38:83:E5:83]",
              "UUID":"7eccfcfa-f334-4042-9dc2-5b5432c33e06",
              "Major":2,
              "Minor":1,
              "Log":[
                 {"Time":"2017-01-10 14:35:19","RSSI":-47,"Measure Power":-51},
                 {"Time":"2017-01-10 14:35:24","RSSI":-49,"Measure Power":-51},
                 {"Time":"2017-01-10 14:35:29","RSSI":-47,"Measure Power":-51},
                 {"Time":"2017-01-10 14:35:34","RSSI":-47,"Measure Power":-51},
                 {"Time":"2017-01-10 14:35:39","RSSI":-48,"Measure Power":-51},   
                 {"Time":"2017-01-10 14:35:44","RSSI":-49,"Measure Power":-51},   
                 {"Time":"2017-01-10 14:35:49","RSSI":-47,"Measure Power":-51},
                 {"Time":"2017-01-10 14:35:55","RSSI":-47,"Measure Power":-51},
                 {"Time":"2017-01-10 14:36:00","RSSI":-47,"Measure Power":-51},   
                 {"Time":"2017-01-10 14:36:05","RSSI":-48,"Measure Power":-51},
                 {"Time":"2017-01-10 14:36:10","RSSI":-47,"Measure Power":-51},
                 {"Time":"2017-01-10 14:36:15","RSSI":-46,"Measure Power":-51},
                 {"Time":"2017-01-10 14:36:20","RSSI":-47,"Measure Power":-51}
               ]
             },
             {"Mac Address":"[E0:F4:4F:F4:98:69]",
              "UUID":"7eccfcfa-f334-4042-9dc2-5b5432c33e06",
              "Major":1,
              "Minor":2,
              "Log":[
                 {"Time":"2017-01-10 14:36:19","RSSI":-77,"Measure Power":-51},
                 {"Time":"2017-01-10 14:36:24","RSSI":-73,"Measure Power":-51},
                 {"Time":"2017-01-10 14:36:29","RSSI":-69,"Measure Power":-51},
                 {"Time":"2017-01-10 14:36:34","RSSI":-70,"Measure Power":-51},
                 {"Time":"2017-01-10 14:36:39","RSSI":-69,"Measure Power":-51},
                 {"Time":"2017-01-10 14:36:44","RSSI":-69,"Measure Power":-51},
                 {"Time":"2017-01-10 14:36:49","RSSI":-70,"Measure Power":-51},
                 {"Time":"2017-01-10 14:36:55","RSSI":-67,"Measure Power":-51},
                 {"Time":"2017-01-10 14:37:00","RSSI":-68,"Measure Power":-51},
                 {"Time":"2017-01-10 14:37:05","RSSI":-68,"Measure Power":-51},
                 {"Time":"2017-01-10 14:37:10","RSSI":-68,"Measure Power":-51},
                 {"Time":"2017-01-10 14:37:15","RSSI":-67,"Measure Power":-51},
                 {"Time":"2017-01-10 14:37:20","RSSI":-70,"Measure Power":-51}
              ]
             }
            ],
            "Events":[
                {"Time":"2017-01-10 14:36:00","Event":"Esto es una prueba"},
                {"Time":"2017-01-10 14:36:05","Event":"Esto es otra prueba"}
            ]}
        }"""
 
        self.response = self.makePostRequest('save', {'data': jsonData1})
        self.response = self.makePostRequest('save', {'data': jsonData2})

    def testSaveJsonData(self):

        jsonResponse = json.loads(self.response.content)

        self.assertEqual(jsonResponse['status'], 'ok')

        self.assertEqual(DetectorDevice.objects.count(), 2)
        self.assertEqual(Beacon.objects.count(), 2)
        self.assertEqual(BeaconLog.objects.count(), 13*2*2)
        self.assertEqual(Event.objects.count(), 2*2)

    def testGetEventsData(self):

        start = '2017-01-09 14:35:59'
        end   = '2017-01-11 14:36:01'
        url = 'getEventsData'

        response = self.makeGetRequest(url, 
                {'start':start,'end':end, 'device': self.deviceId})

        jsonResponse = json.loads(response.content)
        
        self.assertEqual(len(jsonResponse), 2)
        self.assertEqual(jsonResponse[0]['time'], '2017-01-09 14:36:00')
        self.assertEqual(jsonResponse[0]['event'], 'Esto es una prueba')

    def testGetBeaconsData(self):

        start = '2017-01-09 14:37:00'
        end   = '2017-01-11 14:37:25'
        url = 'getBeaconsData'
        
        response = self.makeGetRequest(url, 
                {'start':start,'end':end, 'device': self.deviceId})

        jsonResponse = json.loads(response.content)

        #self.printJson(jsonResponse)
        self.assertEqual(len(jsonResponse), 1)
        self.assertEqual(len(jsonResponse[0]['log']), 5)

    def testGetChartData(self):

        start = '2017-01-09 14:36:00'
        end   = '2017-01-11 14:37:00'
        url = 'getChartData'
        
        response = self.makeGetRequest(url, 
                {'start':start,'end':end, 'device': self.deviceId})

        jsonResponse = json.loads(response.content)
      
        self.assertEqual(len(jsonResponse['columns']), 4)
        self.assertEqual(len(jsonResponse['xs']), 2)
        self.assertEqual(len(jsonResponse['events']), 2)

    def testGetDevicesData(self):

        start = '2017-01-09 14:36:00'
        end   = '2017-01-09 14:37:00'
        url = 'getDevicesData'
        
        response = self.makeGetRequest(url, 
                {'start':start,'end':end})

        jsonResponse = json.loads(response.content)
        
        self.assertEqual(len(jsonResponse), 1)
        self.assertEqual(jsonResponse[0]['deviceId'], self.deviceId)

        end   = '2017-01-11 14:37:00'

        response = self.makeGetRequest(url, 
                {'start':start,'end':end})
        jsonResponse = json.loads(response.content)
        self.assertEqual(len(jsonResponse), 2)
        self.assertEqual(jsonResponse[0]['deviceId'], u'000000000000000')
        self.assertEqual(jsonResponse[1]['deviceId'], self.deviceId)

    def testPlot(self):

        url = 'show'
        response = self.makeGetRequest(url)



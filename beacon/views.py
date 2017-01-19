from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.db import connection
from django.db.models.query import Prefetch
from django.utils import timezone, dateparse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from beacon.models import DetectorDevice, Beacon, BeaconLog, Event

import json

# Create your views here.
class GetChartData(View):
    """ date used by C3js to draw timeseries """

    def __init__(self):
        self.context={}

    def getC3EventsData(self, start, end, deviceId):

        events = GetEventsData().getEvents(start, end, deviceId)
        eventsWithAttrNameChanged = []
        for event in events:
            eventsWithAttrNameChanged.append({
                'value': event['time'],
                'text': event['event'],
                'position': 'middle'
            })
        return eventsWithAttrNameChanged

    def getC3Data(self, start, end, deviceId):
        
        AXIS_PREFIX = 'axis_'

        records = BeaconLog.objects.filter(
                time__range=(start, end), device__externalId=deviceId)
         
        data = {}
        devices = set()
        xs = {}
        for record in records:
            beacon = record.beacon.getDict()
            beaconId = beacon['uuid'] + '-' + beacon['major'] + '-' + beacon['minor']

            if beaconId not in devices:
                devices.add(beaconId)
                data[AXIS_PREFIX + beaconId] = []
                data[beaconId] = []
                xs[beaconId] = AXIS_PREFIX + beaconId

            recordFormatted = record.getDict()
            data[AXIS_PREFIX + beaconId].append(recordFormatted['time'])
            data[beaconId].append(recordFormatted['rssi'])

        dataWithName = []
        for key in data.keys():
            data[key].insert(0, key)
            dataWithName.append(data[key])

        return xs, dataWithName

    def get(self, request):
 
        start    = request.GET['start']
        end      = request.GET['end']
        deviceId = request.GET['device']

        start = dateparse.parse_datetime(start)
        start = timezone.make_aware(start)
        end   = dateparse.parse_datetime(end)
        end   = timezone.make_aware(end)
        
        response = {}
        response['xs'], response['columns'] = self.getC3Data(start, end, deviceId)
        response['events'] = self.getC3EventsData(start, end, deviceId)

        return JsonResponse(response, safe=False)


class GetEventsData(View):

    def __init__(self):
        self.context={}

    def getEvents(self, start, end, deviceId):
 
        events = Event.objects.filter(time__range=(start, end), device__externalId=deviceId)
        eventList = map(lambda x: x.getDict(), events)

        return eventList

    def get(self, request):

        start    = request.GET['start']
        end      = request.GET['end']
        deviceId = request.GET['device']

        start = dateparse.parse_datetime(start)
        start = timezone.make_aware(start)
        end   = dateparse.parse_datetime(end)
        end   = timezone.make_aware(end)

        response = self.getEvents(start, end, deviceId)

        return JsonResponse(response, safe=False)


class GetBeaconsData(View):

    def __init__(self):
        self.context={}

    def get(self, request):
 
        start    = request.GET['start']
        end      = request.GET['end']
        deviceId = request.GET['device']

        start = dateparse.parse_datetime(start)
        start = timezone.make_aware(start)
        end   = dateparse.parse_datetime(end)
        end   = timezone.make_aware(end)

        beacons = Beacon.objects.filter(
                beaconlog__time__range=(start, end), 
                beaconlog__device__externalId=deviceId).distinct()

        response = []
        for beacon in beacons:
            b = beacon.getDict()
            records = BeaconLog.objects.filter(beacon=beacon,
                    time__range=(start, end), device__externalId=deviceId)
            b['log'] = map(lambda x: x.getDict(), records)
            response.append(b)

        return JsonResponse(response, safe=False)


class SaveData(View):

    def __init__(self):
        self.context={}

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(SaveData, self).dispatch(request, *args, **kwargs)

    def post(self, request):
  
        jsonEncoded = request.POST['data']
        jsonDecoded = json.loads(jsonEncoded)
        
        deviceId = jsonDecoded['DeviceID']
        beacons  = jsonDecoded['MeasureData']['Beacons']
        events   = jsonDecoded['MeasureData']['Events']

        if DetectorDevice.objects.filter(externalId=deviceId).exists():
            device = DetectorDevice.objects.get(externalId=deviceId)
        else:
            device = DetectorDevice.objects.create(externalId=deviceId)

        for beacon in beacons:
            if Beacon.objects.filter(macAddr=beacon['Mac Address']).exists():
                beaconObj = Beacon.objects.get(macAddr=beacon['Mac Address'])
            else:
                beaconObj = Beacon.objects.create(
                    macAddr=beacon['Mac Address'],
                    uuid=beacon['UUID'],
                    major=beacon['Major'],
                    minor=beacon['Minor']
                    )

            for record in beacon['Log']:
                time = dateparse.parse_datetime(record['Time'])
                time = timezone.make_aware(time)
                r = BeaconLog.objects.create(
                        time=time,
                        rssi=record['RSSI'],
                        measurePower=record['Measure Power'],
                        beacon=beaconObj,
                        device=device
                        )

        for event in events:
            time = dateparse.parse_datetime(event['Time'])
            time = timezone.make_aware(time)
            e = Event.objects.create(
                    time=time,
                    event=event['Event'],
                    device=device
                    )

        response = {}
        response['status'] = 'ok'
        return JsonResponse(response, safe=False)


class Plot(View):

    def __init__(self):
        self.context={}

    def get(self, request):
        template = "beacon.html"

        return render(request, template, self.context)


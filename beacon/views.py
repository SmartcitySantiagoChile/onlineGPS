from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.db import connection
from django.utils import timezone, dateparse

from beacon.models import Beacon, BeaconLog, Event

import json

# Create your views here.
class GetBeaconsData(View):

    def __init__(self):
        self.context={}

    def get(self, request):
 
        start = request.GET['start']
        end   = request.GET['end']

        start = dateparse.parse_datetime(start)
        start = timezone.make_aware(start)
        end   = dateparse.parse_datetime(end)
        end   = timezone.make_aware(end)
        
        beacons = Beacon.objects.filter(
                beaconlog__time__range=(start, end)).distinct()

        response = []
        for beacon in beacons:
            b = beacon.getDict()
            log = []
            records = BeaconLog.objects.filter(beacon=beacon, 
                    time__range=(start, end))
            for record in records:
                log.append(record.getDict())
            b['log'] = log
            response.append(b)

        return JsonResponse(response, safe=False)


class GetEventsData(View):

    def __init__(self):
        self.context={}

    def get(self, request):
 
        start = request.GET['start']
        end   = request.GET['end']

        start = dateparse.parse_datetime(start)
        start = timezone.make_aware(start)
        end   = dateparse.parse_datetime(end)
        end   = timezone.make_aware(end)

        events = Event.objects.filter(time__range=(start, end))

        response = []
        for event in events:
            response.append(event.getDict())

        return JsonResponse(response, safe=False)


class SaveData(View):

    def __init__(self):
        self.context={}

    def post(self, request):
  
        jsonEncoded = request.POST['data']
        jsonDecoded = json.loads(jsonEncoded)

        beacons = jsonDecoded['Beacons']
        events  = jsonDecoded['Events']

        for beacon in beacons:
            try:
                b = Beacon.objects.get(macAddr=beacon['Mac Address'])
            except Beacon.DoesNotExist:
                b = Beacon(
                    macAddr=beacon['Mac Address'],
                    uuid=beacon['UUID'],
                    major=beacon['Major'],
                    minor=beacon['Minor']
                    )
                b.save()

            for record in beacon['Log']:
                time = dateparse.parse_datetime(record['Time'])
                time = timezone.make_aware(time)
                r = BeaconLog(
                        time=time,
                        rssi=record['RSSI'],
                        measurePower=record['Measure Power'],
                        beacon=b
                        )
                r.save()

        for event in events:
            time = dateparse.parse_datetime(event['Time'])
            time = timezone.make_aware(time)
            e = Event(
                    time=time,
                    event=event['Event']
                    )
            e.save()

        response = {}
        response['status'] = 'ok'
        return JsonResponse(response, safe=False)


class Plot(View):

    def __init__(self):
        self.context={}

    def get(self, request):
        template = "beacon.html"

        return render(request, template, self.context)


from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from django.utils import timezone, dateparse
import datetime

# model
from transappbusposition.models import Ultimo15MinGps

class GetEstimatedBusPosition(View):
    ''' This class requests to the database the bus position based on date '''

    #def __init__(self):
    #	self.context={}

    def get(self, request):
        """ it gives the nearest GPS record respect to time for a bus """

        licencePlate = request.GET['licencePlate']
        fLicencePlate = licencePlate[:4] + '-' + licencePlate[-2:]
        time = request.GET['time']

        #licencePlate = "CJRB-73"
        #time = "2016-11-12T15:58:00"
        # debo pasarle la hora con 3 horas menos para que matchee
        time = dateparse.parse_datetime(time)
        offsetTime = time - datetime.timedelta(hours=3)
        #time = timezone.make_aware(time)
        
        response = {}
        response['error'] = False

        closestGreaterQS = Ultimo15MinGps.objects.filter(tiempo__gte=offsetTime, patente=fLicencePlate).order_by('tiempo')
        closestLessQS    = Ultimo15MinGps.objects.filter(tiempo__lt=offsetTime, patente=fLicencePlate).order_by('-tiempo')
        #response['query'] = str(closestGreaterQS.query)

        #response['g'] = len(closestGreaterQS)
        #response['l'] = len(closestLessQS)
	#return JsonResponse(response, safe=False)

        try:
            if closestGreaterQS.count() > 0 and closestLessQS.count() > 0:
                #response['gtime'] = str(closestGreaterQS[0].tiempo - time)
                #response['ltime'] = str(time - closestLessQS[0].tiempo)
                if (closestGreaterQS[0].tiempo - time) > (time - closestLessQS[0].tiempo):
                    closestTime = closestLessQS[0]
                    response['diffTime'] = str(time - closestLessQS[0].tiempo)
                else:
                    closestTime = closestGreaterQS[0]
                    response['diffTime'] = str(closestGreaterQS[0].tiempo - time)
            elif closestGreaterQS.count() > 0 and closestLessQS.count() == 0:
                    closestTime = closestGreaterQS[0]
                    response['diffTime'] = str(closestGreaterQS[0].tiempo - time)
            elif closestGreaterQS.count() == 0 and closestLessQS.count() > 0:
                    closestTime = closestLessQS[0]
                    response['diffTime'] = str(time - closestLessQS[0].tiempo)
            else:
                raise Exception('There is no closest object because there are no objects.')

            response['machine'] = {}
	    response['machine']['licencePlate'] = licencePlate#closestTime.patente
            response['machine']['route'] = closestTime.servicio
            response['nearestGpsPoint'] = {}
            response['nearestGpsPoint']['latitude'] = closestTime.latitud
            response['nearestGpsPoint']['longitude'] = closestTime.longitud
	    response['nearestGpsPoint']['time'] = closestTime.tiempo

        except Exception as e:
            response['error'] = True
            response['message'] = str(e)
            response['machine'] =  {}

	return JsonResponse(response, safe=False)


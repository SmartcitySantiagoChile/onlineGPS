from django.db import models
from django.utils import timezone

# Create your models here.

def formatDateTime(dateTime):
    return timezone.localtime(dateTime).strftime("%Y-%m-%d %H:%M:%S")

class Beacon(models.Model):
    macAddr = models.CharField(max_length=20)
    uuid    = models.UUIDField(editable=False)
    major   = models.CharField(max_length=10, null=False)
    minor   = models.CharField(max_length=10, null=False)

    def getDict(self):
        dict = {}
        dict['macAddr'] = self.macAddr
        dict['uuid'] = str(self.uuid)
        dict['major'] = self.major
        dict['minor'] = self.minor
        return dict

    class Meta:
        unique_together = ('uuid', 'major', 'minor')

class BeaconLog(models.Model):
    time         = models.DateTimeField(null=False)
    rssi         = models.IntegerField(null=False)
    measurePower = models.IntegerField(null=False)
    beacon       = models.ForeignKey(Beacon, on_delete=models.CASCADE)

    def __str__(self):
        return "{} | {} | {}".format(self.time, self.rssi, self.measurePower)

    def getDict(self):
        dict = {}
        dict['time'] = formatDateTime(self.time)
        dict['rssi'] = self.rssi
        dict['measurePower'] = self.measurePower
        return dict


class Event(models.Model):
    time  = models.DateTimeField(null=False)
    event = models.TextField(null=False)

    def getDict(self):
        dict = {}
        dict['time'] = formatDateTime(self.time)
        dict['event'] = self.event
        return dict


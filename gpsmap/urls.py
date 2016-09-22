from django.conf.urls import url
from . import views
from gpsmap.views import MapHandler, GetMapPositions, GetMapPositionsByService, ServiceHandler

urlpatterns = [
	url(r'^show$', MapHandler.as_view()),
	url(r'^busLocations$', GetMapPositions.as_view()),
	url(r'^getService/(?P<service>\w+)/(?P<direction>\w{1})$', GetMapPositionsByService.as_view()),
	url(r'^service$', ServiceHandler.as_view()),
]

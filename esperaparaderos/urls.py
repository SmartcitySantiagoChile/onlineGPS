from django.conf.urls import url
from . import views
from esperaparaderos.views import GetWaitingUsersByBusStop, WaitingUsersByBusStopMapHandler, GetMostDelayedBusesByBusStop

urlpatterns = [
	url(r'^show$', WaitingUsersByBusStopMapHandler.as_view()),
	url(r'^getMostPopulatedBusStops/(?P<quantity>[0-9]+)$', GetWaitingUsersByBusStop.as_view()),
	url(r'^getMostDelayedBusesToBusStops/(?P<quantity>[0-9]+)$', GetMostDelayedBusesByBusStop.as_view()),
]

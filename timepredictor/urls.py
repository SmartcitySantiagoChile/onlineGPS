from django.conf.urls import url
from . import views
from timepredictor.views import MapHandler, GetEstimatedTimes, GetBusPosition

urlpatterns = [
	url(r'^show$', MapHandler.as_view()),
	url(r'^getEstimatedTimes/(?P<licencePlate>[0-9,\w,-]{6,8})$', GetEstimatedTimes.as_view()),
	url(r'^getBusPosition/(?P<licencePlate>[0-9,\w,-]{6,8})$', GetBusPosition.as_view()),
]

from django.conf.urls import url
from . import views
from beacon.views import Plot, SaveData, GetBeaconsData, GetEventsData, GetChartData, GetDevicesData

urlpatterns = [
	url(r'^show$', Plot.as_view()),
	url(r'^getChartData$', GetChartData.as_view()),
	url(r'^save$', SaveData.as_view()),
	url(r'^getBeaconsData$', GetBeaconsData.as_view()),
	url(r'^getEventsData$', GetEventsData.as_view()),
	url(r'^getDevicesData$', GetDevicesData.as_view()),
]

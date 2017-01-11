from django.conf.urls import url
from . import views
from beacon.views import Plot, SaveData, GetBeaconsData, GetEventsData

urlpatterns = [
	url(r'^show$', Plot.as_view()),
	url(r'^save$', SaveData.as_view()),
	url(r'^getBeaconsData$', GetBeaconsData.as_view()),
	url(r'^getEventsData$', GetEventsData.as_view()),
]

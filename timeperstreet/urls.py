from django.conf.urls import url
from . import views
from timeperstreet.views import StreetTimeMapHandler, GetStreetData, GetPOIData

urlpatterns = [
	url(r'^show$', StreetTimeMapHandler.as_view()),
	url(r'^getStreetData$', GetStreetData.as_view()),
	url(r'^getPOIData$', GetPOIData.as_view()),
]

from django.conf.urls import url
from . import views
from timeperstreet.views import StreetMapHandler, GetStreetData, GetPOIData

urlpatterns = [
	url(r'^show$', StreetMapHandler.as_view()),
	url(r'^getStreetData$', GetStreetData.as_view()),
	url(r'^getPOIData$', GetPOIData.as_view()),
]

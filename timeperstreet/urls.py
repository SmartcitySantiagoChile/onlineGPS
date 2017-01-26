from django.conf.urls import url
from . import views
from timeperstreet.views import StreetTimeMapHandler, StreetTimeTableMapHandler, GetStreetTableData, GetStreetData, GetPOIData

urlpatterns = [
	url(r'^show$', StreetTimeMapHandler.as_view()),
	url(r'^getStreetData$', GetStreetData.as_view()),
	url(r'^getPOIData$', GetPOIData.as_view()),
	url(r'^show2$', StreetTimeTableMapHandler.as_view()),
	url(r'^getStreetTableData$', GetStreetTableData.as_view()),
]

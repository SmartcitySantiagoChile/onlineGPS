from django.conf.urls import url
from . import views
from velocityperstreet.views import StreetVelocityMapHandler, GetStreetData, GetPOIData

urlpatterns = [
	url(r'^show$', StreetVelocityMapHandler.as_view()),
	url(r'^getStreetData$', GetStreetData.as_view()),
	url(r'^getPOIData$', GetPOIData.as_view()),
]

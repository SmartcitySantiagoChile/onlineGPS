from django.conf.urls import url
from . import views
from timeperstreet.views import StreetMapHandler, GetStreetData

urlpatterns = [
	url(r'^show$', StreetMapHandler.as_view()),
	url(r'^getStreetData$', GetStreetData.as_view()),
]

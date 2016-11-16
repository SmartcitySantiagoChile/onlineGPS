from django.conf.urls import url
from . import views
from dtpmvelocities.views import MapHandler

urlpatterns = [
	url(r'^show$', MapHandler.as_view()),
]

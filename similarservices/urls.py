from django.conf.urls import url
from . import views
from similarservices.views import IndexHandler

urlpatterns = [
	url(r'^show$', IndexHandler.as_view()),
]

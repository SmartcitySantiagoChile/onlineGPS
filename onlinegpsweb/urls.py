"""gpsonlineweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^map/', include('gpsmap.urls')),
    url(r'^waitingUsersByBusStop/', include('esperaparaderos.urls')),
    url(r'^timePerStreet/', include('timeperstreet.urls')),
    url(r'^velocityPerStreet/', include('velocityperstreet.urls')),
    url(r'^similarservices/', include('similarservices.urls')),
    url(r'^timePredictor/', include('timepredictor.urls')),
    url(r'^transappBusPosition/', include('transappbusposition.urls')),
    url(r'^dtpmVelocities/', include('dtpmvelocities.urls')),
    url(r'^drawRoute/', include('drawroute.urls')),
    url(r'^beacon/', include('beacon.urls')),
    url(r'^dailybusesinfo/', include('dailybusesinfo.urls')),
    url(r'^speedbyroute/', include('speedbyroute.urls')),
    url(r'^alerts/', include('alerts.urls')),
]

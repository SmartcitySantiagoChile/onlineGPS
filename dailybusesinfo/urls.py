from django.conf.urls import url, include
from django.contrib import admin
from dailybusesinfo.views import Info, GetBusesInfo

urlpatterns = [
    url(r'^show$', Info.as_view()),
    url(r'^getBusesInfo$', GetBusesInfo.as_view()),
]



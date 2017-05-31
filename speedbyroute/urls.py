from django.conf.urls import url

from . import views
from speedbyroute.views import GetInfoRouteData

urlpatterns = [
    url(r'^getOnlineRouteSpeeds/(?P<routeName>[0-9,\w,-]{3,10})$', GetInfoRouteData.as_view()),
]
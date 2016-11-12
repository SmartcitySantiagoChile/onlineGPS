from django.conf.urls import url
from . import views
from transappbusposition.views import GetEstimatedBusPosition

urlpatterns = [
        url(r'^getEstimatedPosition$', GetEstimatedBusPosition.as_view()),
]

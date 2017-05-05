from django.conf.urls import url
from . import views
from alerts.views import AlertTableHandler, GetTableData

urlpatterns = [
	url(r'^show$', AlertTableHandler.as_view()),
	url(r'^getData$', GetTableData.as_view()),
]

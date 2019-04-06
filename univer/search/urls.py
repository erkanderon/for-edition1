from django.conf.urls import url
from . import views

app_name = "search"

urlpatterns = [

    url(r'^courses/$', views.SearchPageView.as_view(), name='searchview'),
]
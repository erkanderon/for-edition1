from django.conf.urls import url
from . import views

app_name = "homepage"

urlpatterns = [

    url(r'^$', views.HomePageView.as_view(), name='homeview'),
    ##url(r'^$', views.HomeView.as_view(), name='blog'),
    ##url(r'^about/$', views.AboutUsView.as_view(), name='about'),
    ##url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    ##url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='post_detail'),


    
]
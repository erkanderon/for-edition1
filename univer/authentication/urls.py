from django.conf.urls import url
from . import views

app_name = "auth"

urlpatterns = [

    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    ##url(r'^$', views.HomeView.as_view(), name='blog'),
    ##url(r'^about/$', views.AboutUsView.as_view(), name='about'),
    ##url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    ##url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='post_detail'),


    
]
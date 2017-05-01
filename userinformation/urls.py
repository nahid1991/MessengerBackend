from django.conf.urls import url, include
from userinformation import views

urlpatterns = [
    url(r'^login/$', views.facebook_login),
]
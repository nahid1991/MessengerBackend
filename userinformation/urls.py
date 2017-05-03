from django.conf.urls import url, include
from userinformation import views

urlpatterns = [
    url(r'^facebook_login/$', views.facebook_login),
    url(r'^user_info/$', views.get_user_info),
]
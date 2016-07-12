from django.conf.urls import patterns, url
from django.contrib import admin

from . import views

admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^location/fetch/$', views.UserLocationFetching.as_view(), name='weixin_fetch_user_location'),
    url(r'^(\w+)/$', views.Weixin.as_view(), name='weixin_entry'),
)

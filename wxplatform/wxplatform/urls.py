from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wx.views.home', name='home'),
    url(r'^wx/', include(wxaccount.urls)),
    url(r'^admin/', include(admin.site.urls)),
)

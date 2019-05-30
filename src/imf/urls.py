"""imf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from core.views import (Home, Seminars, AboutUs, Team, Services,
                        Contact)

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^aboutus/$', AboutUs.as_view(), name='aboutus'),
    url(r'^team/$', Team.as_view(), name='team'),
    url(r'^services/$', Services.as_view(), name='services'),
    url(r'^seminars/$', Seminars.as_view(), name='seminars'),
    url(r'^contact/$', Contact.as_view(), name='contact'),
    url(r'^admin/', admin.site.urls),
]

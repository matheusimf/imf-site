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
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path

from core.views import (HomeView, AboutUsView, TeamView, ServicesView,
                        ContactView)
from core.sitemaps import HomeViewSitemap, StaticViewSitemap
from seminars.sitemaps import SeminarViewSitemap, SeminarTypeViewSitemap

sitemaps = {
    'home': HomeViewSitemap,
    'static': StaticViewSitemap,
    'seminar_type': SeminarTypeViewSitemap,
    'seminar': SeminarViewSitemap,
}

urlpatterns = [
    re_path(r'^$', HomeView.as_view(), name='home'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    path('sobre-nos/', AboutUsView.as_view(), name='aboutus'),
    path('time/', TeamView.as_view(), name='team'),
    path('servicos/', ServicesView.as_view(), name='services'),
    path('cursos/', include(('seminars.urls', 'seminars'))),
    path('contato/', ContactView.as_view(), name='contact'),
    path('admin/', admin.site.urls),
]

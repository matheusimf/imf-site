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
from django.urls import include, path, re_path

from core.views import Home, AboutUs, Team, Services, Contact

urlpatterns = [
    re_path(r'^$', Home.as_view(), name='home'),
    path('sobre-nos/', AboutUs.as_view(), name='aboutus'),
    path('time/', Team.as_view(), name='team'),
    path('servicos/', Services.as_view(), name='services'),
    path('cursos/', include(('seminars.urls', 'seminars'))),
    path('contato/', Contact.as_view(), name='contact'),
    path('admin/', admin.site.urls),
]

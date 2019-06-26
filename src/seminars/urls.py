from django.urls import include, path, re_path

from .views import Seminars, BasicDNASeminar, AdvancedDNASeminar

urlpatterns = [
    re_path(r'^$', Seminars.as_view(), name='seminars'),
    path('dna-basico/', BasicDNASeminar.as_view(), name='basic-dna'),
    path('dna-avancado/', AdvancedDNASeminar.as_view(), name='advanced-dna'),
]

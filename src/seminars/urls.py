from django.urls import include, path, re_path

from .views import Seminars

urlpatterns = [
    re_path(r'^$', Seminars.as_view(), name='seminars'),
]

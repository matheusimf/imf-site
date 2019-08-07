from django.urls import include, path, re_path

from .views import (Seminars, BaseSeminar, SeminarsSchedule)


urlpatterns = [
    re_path(r'^$', Seminars.as_view(), name='seminars'),
    path('schedule/', SeminarsSchedule.as_view(), name='schedule'),
    re_path('(?P<slug>[-\w]+)/$', BaseSeminar.as_view(), name='base-seminar'),
]

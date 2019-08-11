from django.urls import include, path, re_path

from .views import (Seminars, BaseSeminar, DateSeminar, SeminarsSchedule)


urlpatterns = [
    re_path(r'^$', Seminars.as_view(), name='seminars'),
    path('agenda/', SeminarsSchedule.as_view(), name='schedule'),
    re_path('(?P<slug>[-\w]+)/(?P<date>\d{2}-\d{2}-\d{4})/$',
            DateSeminar.as_view(), name='seminar-date'),
    re_path('(?P<slug>[-\w]+)/$', BaseSeminar.as_view(), name='base-seminar'),
]

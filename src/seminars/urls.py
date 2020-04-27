from django.urls import include, path, re_path

from .views import (SeminarsView, BaseSeminarView, DateSeminarView,
                    SeminarsScheduleView, SeminarInscriptionView)


urlpatterns = [
    re_path(r'^$', SeminarsView.as_view(), name='seminars'),
    path('agenda/', SeminarsScheduleView.as_view(), name='schedule'),
    path('seminar-inscription/', SeminarInscriptionView.as_view(), name='inscription'),
    re_path('(?P<slug>[-\w]+)/(?P<date>\d{2}-\d{2}-\d{4})/$',
            DateSeminarView.as_view(), name='seminar-date'),
    re_path('(?P<slug>[-\w]+)/$', BaseSeminarView.as_view(), name='base-seminar'),
]

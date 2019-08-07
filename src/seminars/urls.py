from django.urls import include, path, re_path

from .views import (Seminars, AdvancedDNASeminar,
                    YouAndCreatorSeminar, IntuitiveAnatomySeminar,
                    InnerCircleSeminar, DNA3Seminar, RainbowChildrenSeminar,
                    DigDeeperSeminar, ManifestingSeminar, EarthSeminar,
                    WorldRelationsSeminar, SignificantOtherSeminar,
                    PlanesSeminar, DiseaseSeminar, BaseSeminar)


urlpatterns = [
    re_path(r'^$', Seminars.as_view(), name='seminars'),
    re_path('(?P<slug>[-\w]+)/$', BaseSeminar.as_view(), name='base-seminar'),
]

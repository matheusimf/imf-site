from django.urls import include, path, re_path

from .views import (Seminars, BasicDNASeminar, AdvancedDNASeminar, YouAndCreatorSeminar,
                    IntuitiveAnatomySeminar, InnerCircleSeminar, DNA3Seminar,
                    RainbowChildrenSeminar, DigDeeperSeminar, ManifestingSeminar,
                    SignificantOtherSeminar, EarthSeminar, WorldRelationsSeminar,
                    PlanesSeminar, DiseaseSeminar)

urlpatterns = [
    re_path(r'^$', Seminars.as_view(), name='seminars'),
    path('dna-basico/', BasicDNASeminar.as_view(), name='basic-dna'),
    path('dna-avancado/', AdvancedDNASeminar.as_view(), name='advanced-dna'),
    path('digging/', DigDeeperSeminar.as_view(), name='dig-deeper'),
    path('manifestacao-e-abundancia/', ManifestingSeminar.as_view(), name='manifesting'),
    path('voce-e-seu-parceiro/', SignificantOtherSeminar.as_view(), name='significant-other'),
    path('voce-e-o-criador/', YouAndCreatorSeminar.as_view(), name='you-and-creator'),
    path('voce-e-o-terra/', EarthSeminar.as_view(), name='you-and-earth'),
    path('anatomia-intuitiva/', IntuitiveAnatomySeminar.as_view(), name='intuitive-anatomy'),
    path('relacoes-mundiais/', WorldRelationsSeminar.as_view(), name='world-relations'),
    path('voce-e-seu-circulo-intimo/', InnerCircleSeminar.as_view(), name='inner-circle'),
    path('dna3/', DNA3Seminar.as_view(), name='dna3'),
    path('planos-de-existencia/', PlanesSeminar.as_view(), name='planes'),
    path('doencas-e-desordens/', DiseaseSeminar.as_view(), name='disease-and-disorder'),
    path('crianca-arco-iris/', RainbowChildrenSeminar.as_view(), name='rainbow-children'),
]

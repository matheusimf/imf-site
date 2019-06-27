from django.urls import include, path, re_path

from .views import (Seminars, BasicDNASeminar, AdvancedDNASeminar, YouAndCreatorSeminar,
                    IntuitiveAnatomySeminar, InnerCircleSeminar, DNA3Seminar,
                    RainbowChildrenSeminar, DigDeeperSeminar, ManifestingSeminar)

urlpatterns = [
    re_path(r'^$', Seminars.as_view(), name='seminars'),
    path('dna-basico/', BasicDNASeminar.as_view(), name='basic-dna'),
    path('dna-avancado/', AdvancedDNASeminar.as_view(), name='advanced-dna'),
    path('digging/', DigDeeperSeminar.as_view(), name='dig-deeper'),
    path('manifestacao-e-abundancia/', ManifestingSeminar.as_view(), name='manifesting'),
    path('voce-e-o-criador/', YouAndCreatorSeminar.as_view(), name='you-and-creator'),
    path('anatomia-intuitiva/', IntuitiveAnatomySeminar.as_view(), name='intuitive-anatomy'),
    path('voce-e-seu-circulo-intimo/', InnerCircleSeminar.as_view(), name='inner-circle'),
    path('dna3/', DNA3Seminar.as_view(), name='dna3'),
    path('crianca-arco-iris/', RainbowChildrenSeminar.as_view(), name='rainbow-children'),
]

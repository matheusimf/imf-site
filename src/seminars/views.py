from django.http import Http404
from django.shortcuts import render
from django.views.generic import View

from .models import SeminarType


class Seminars(View):
    template_name = 'seminars/seminars.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


class BaseSeminar(View):
    template_name = 'seminars/base-seminars.html'

    def get(self, request, *args, **kwargs):
        seminar_url = self.kwargs['slug']

        seminar = SeminarType.objects.filter(url=seminar_url).last()

        if not seminar:
            raise Http404()

        context = {
            'seminar': seminar,
        }

        return render(request, self.template_name, context)

class BasicDNASeminar(BaseSeminar):
    template_name = 'seminars/base-seminars.html'

class AdvancedDNASeminar(BaseSeminar):
    template_name = 'seminars/advanced-dna.html'

class DigDeeperSeminar(BaseSeminar):
    template_name = 'seminars/dig-deeper.html'

class ManifestingSeminar(BaseSeminar):
    template_name = 'seminars/manifesting.html'

class SignificantOtherSeminar(BaseSeminar):
    template_name = 'seminars/significant-other.html'

class YouAndCreatorSeminar(BaseSeminar):
    template_name = 'seminars/you-and-creator.html'

class InnerCircleSeminar(BaseSeminar):
    template_name = 'seminars/inner-circle.html'

class EarthSeminar(BaseSeminar):
    template_name = 'seminars/you-and-earth.html'

class WorldRelationsSeminar(BaseSeminar):
    template_name = 'seminars/world-relations.html'

class IntuitiveAnatomySeminar(BaseSeminar):
    template_name = 'seminars/intuitive-anatomy.html'

class PlanesSeminar(BaseSeminar):
    template_name = 'seminars/planes.html'

class DNA3Seminar(BaseSeminar):
    template_name = 'seminars/dna3.html'

class DiseaseSeminar(BaseSeminar):
    template_name = 'seminars/disease-and-disorder.html'

class RainbowChildrenSeminar(BaseSeminar):
    template_name = 'seminars/rainbow-children.html'

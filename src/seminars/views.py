from django.shortcuts import render
from django.views.generic import View


class Seminars(View):
    template_name = 'seminars/seminars.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


class BaseSeminar(View):
    template_name = 'seminars/base-seminars.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

class BasicDNASeminar(BaseSeminar):
    template_name = 'seminars/basic-dna.html'

class AdvancedDNASeminar(BaseSeminar):
    template_name = 'seminars/advanced-dna.html'

class YouAndCreatorSeminar(BaseSeminar):
    template_name = 'seminars/you-and-creator.html'

class InnerCircleSeminar(BaseSeminar):
    template_name = 'seminars/inner-circle.html'

class IntuitiveAnatomySeminar(BaseSeminar):
    template_name = 'seminars/intuitive-anatomy.html'

class DNA3Seminar(BaseSeminar):
    template_name = 'seminars/dna3.html'

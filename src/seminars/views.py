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
    template_name = 'seminars/base-seminars.html'

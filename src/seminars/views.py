from django.shortcuts import render
from django.views.generic import View


class Seminars(View):
    template_name = 'core/seminars.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

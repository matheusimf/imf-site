from django.shortcuts import render
from django.views.generic import View

class Home(View):
    template_name = 'core/home.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

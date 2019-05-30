from django.shortcuts import render
from django.views.generic import View


class Home(View):
    template_name = 'core/home.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


class Seminars(Home):
    template_name = 'core/seminars.html'


class AboutUs(Home):
    template_name = 'core/aboutus.html'


class Team(Home):
    template_name = 'core/team.html'


class Services(Home):
    template_name = 'core/services.html'


class Contact(Home):
    template_name = 'core/contact.html'

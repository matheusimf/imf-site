from django.shortcuts import render
from django.views.generic import View

from seminars.models import Seminar


class Home(View):
    template_name = 'core/home.html'

    def get(self, request, *args, **kwargs):
        # get the seminars and order then by start date
        seminars = Seminar.objects.filter(seminar_status=0)
        ordered_seminars = seminars.order_by('start_date')

        # get the next 6 seminars split in 2 different objects
        next_first_seminars = ordered_seminars[:3]
        next_last_seminars = ordered_seminars[3:6]

        next_seminars = [next_first_seminars, next_last_seminars]

        context = {
            'next_seminars': next_seminars,
        }
        return render(request, self.template_name, context)


class AboutUs(Home):
    template_name = 'core/aboutus.html'


class Team(Home):
    template_name = 'core/team.html'


class Services(Home):
    template_name = 'core/services.html'


class Contact(Home):
    template_name = 'core/contact.html'

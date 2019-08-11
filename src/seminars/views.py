from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render
from django.views.generic import View

import datetime

from .models import Seminar, SeminarType


class Seminars(View):
    template_name = 'seminars/seminars.html'

    def get(self, request, *args, **kwargs):
        seminars_type = SeminarType.objects.all()
        paginated_seminars = Paginator(seminars_type, 4)

        # We will have a list of seminars with sublists of 4 seminars
        # to display the right way on template
        seminar_list = []
        for page in paginated_seminars.page_range:
            seminar_list.append(paginated_seminars.get_page(page))

        context = {
            'seminar_list': seminar_list,
        }
        return render(request, self.template_name, context)


class BaseSeminar(View):
    template_name = 'seminars/base-seminars.html'

    def get(self, request, *args, **kwargs):
        seminar_url = self.kwargs['slug']

        seminar_type = SeminarType.objects.filter(url=seminar_url).last()

        if not seminar_type:
            raise Http404()

        next_seminars = Seminar.objects.filter(
            seminar_status=Seminar.ACTIVE, seminar_type=seminar_type
        )

        context = {
            'seminar_type': seminar_type,
            'next_seminars': next_seminars,
        }

        return render(request, self.template_name, context)


class DateSeminar(View):
    template_name = 'seminars/specific_seminar.html'

    def get(self, request, *args, **kwargs):
        #import ipdb; ipdb.set_trace()
        seminar_url = self.kwargs['slug']
        date = self.kwargs['date']

        try:
            seminar_date = datetime.datetime.strptime(date, "%d-%m-%Y")
        except ValueError:
            raise Http404()

        try:
            seminar = Seminar.objects.get(
                seminar_type__url=seminar_url, start_date=seminar_date
            )
        except ObjectDoesNotExist:
            raise Http404()

        context = {
            'seminar': seminar,
            'seminar_type': seminar.seminar_type,
        }

        return render(request, self.template_name, context)


class SeminarsSchedule(View):
    template_name = 'seminars/seminars_schedule.html'

    def get(self, request, *args, **kwargs):
        # get the seminars and order then by start date
        seminars = Seminar.objects.filter(seminar_status=0)
        ordered_seminars = seminars.order_by('start_date')
        paginated_seminars = Paginator(ordered_seminars, 3)

        # We will have a list of seminars with sublists of 3 seminars
        # to display the right way on template
        seminar_list = []
        for page in paginated_seminars.page_range:
            seminar_list.append(paginated_seminars.get_page(page))

        context = {
            'seminar_list': seminar_list,
        }
        return render(request, self.template_name, context)

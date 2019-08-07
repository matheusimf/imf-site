from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render
from django.views.generic import View

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

        seminar = SeminarType.objects.filter(url=seminar_url).last()

        if not seminar:
            raise Http404()

        context = {
            'seminar': seminar,
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

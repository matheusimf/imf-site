from django.contrib import sitemaps
from django.urls import reverse

from seminars.models import Seminar, SeminarType


class SeminarTypeViewSitemap(sitemaps.Sitemap):
    priority = 0.8
    changefreq = 'yearly'

    def items(self):
        return SeminarType.objects.all()

    def location(self, item):
        return '/%s'%(item.url)


class SeminarViewSitemap(sitemaps.Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return Seminar.objects.filter(seminar_status=Seminar.ACTIVE)

    def location(self, item):
        seminar_type = item.seminar_type.url
        date = item.start_date.strftime('%d/%m/%y')
        return '/%s/%s'%(seminar_type, date)

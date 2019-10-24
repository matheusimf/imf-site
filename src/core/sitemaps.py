from django.contrib import sitemaps
from django.urls import reverse


class HomeViewSitemap(sitemaps.Sitemap):
    priority = 1
    changefreq = 'yearly'

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.8
    changefreq = 'yearly'

    def items(self):
        return ['aboutus', 'team', 'services', 'contact']

    def location(self, item):
        return reverse(item)

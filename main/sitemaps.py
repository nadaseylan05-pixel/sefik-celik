from django.contrib.sitemaps import Sitemap
from .models import (
    BlogPost,
    #Employee,
    TeamPage,
    SiteContent,
    AboutPage,
    ServicesPage,
    ServiceArea,
    BlogPage,
    Karier
)

# -------------------- Services --------------------
class ServicesPageSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ServicesPage.objects.all()
    def lastmod(self, obj):
        return obj.updated_at

# -------------------- Team --------------------
class TeamPageSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return TeamPage.objects.all()
    def lastmod(self, obj):
        return obj.updated_at

# -------------------- Employees --------------------
'''
class EmployeeSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.4

    def items(self):
        return Employee.objects.all()
'''
'''
# -------------------- Site Content --------------------
class SiteContentSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return SiteContent.objects.all()
    def lastmod(self, obj):
        return obj.updated_at
'''
# -------------------- About Page --------------------
class AboutPageSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return AboutPage.objects.all()
    def lastmod(self, obj):
        return obj.updated_at
'''
# -------------------- Service Area --------------------
class ServiceAreaSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return ServiceArea.objects.all()
    def lastmod(self, obj):
        return obj.updated_at
'''    

# -------------------- Blog Pages --------------------
class BlogPageSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return BlogPage.objects.all()
    

# -------------------- Blog Posts --------------------

'''
class BlogPostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return BlogPost.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

 '''  
# -------------------- Careers --------------------
class KarierSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.4

    def items(self):
        return Karier.objects.all()
    def lastmod(self, obj):
        return obj.updated_at

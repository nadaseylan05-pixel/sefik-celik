from django.urls import path 
from .views import home ,hakimizda,blog,ekibimiz,work_areas_view,blog,iletişim,kariyer

from django.contrib.sitemaps.views import sitemap
from main.sitemaps import  BlogPageSitemap,SiteContentSitemap, TeamPageSitemap, AboutPageSitemap, ServicesPageSitemap, KarierSitemap

sitemaps = {
    "blog": BlogPageSitemap,
    "site-content": SiteContentSitemap,
    "team": TeamPageSitemap,
    "about": AboutPageSitemap,
    "services": ServicesPageSitemap,
    "career": KarierSitemap,
}

urlpatterns=[
    path('',home, name='home'),
    path('hakimizda',hakimizda,name='hakimizda'),
    path('blog',blog,name='blog'),
    path('ekibimiz',ekibimiz,name='ekibimiz'),
    path('alanlarimiz/', work_areas_view, name='Çalışma_alanları'),
    path('blog/', blog, name='blog'),
    path('iletişim/', iletişim, name='iletişim'),
    #path('send_message/', send_message, name='send_message'),
    path('kariyer/', kariyer, name='kariyer'),
    #path('sitemaps.xml', sitemap, {'sitemaps':sitemap}, name='django.contrib.sitemaps.views.sitemaps'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),    
]
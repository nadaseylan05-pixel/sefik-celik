from django.db import models
from django.utils import timezone
# Create your models here.
# =========================
# 1. Şirket Bilgisi (Tek kayıt)
# =========================
class CompanyInfo(models.Model):
    company_name = models.CharField("Şirket Adı", max_length=200)
    address = models.CharField("Adres", max_length=300)
    phone = models.CharField("Telefon", max_length=50)
    email = models.EmailField("E-posta")
    website = models.URLField("Web Sitesi", blank=True)

    facebook = models.URLField("Facebook", blank=True)
    instagram = models.URLField("Instagram", blank=True)
    linkedin = models.URLField("LinkedIn", blank=True)
    lat = models.DecimalField("Latitude", max_digits=9, decimal_places=6, default=0.0)
    lng = models.DecimalField("Longitude", max_digits=9, decimal_places=6, default=0.0)
    homepage_image = models.ImageField("Ana Sayfa Resmi", upload_to="homepage_images/", blank=True, null=True)
    comminication_image = models.ImageField("İletişim Resmi", upload_to="comminication_images/", blank=True, null=True)
    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = "Şirket Bilgisi"
        verbose_name_plural = "Şirket Bilgisi"


# =========================
# 2. Çalışanlar
# =========================

class TeamPage(models.Model):
    hero_image = models.ImageField(upload_to='team_hero/', default='team_hero/default_team_hero.jpg')
    title = models.CharField("Ekip Sayfası Başlığı", max_length=200, default="Ekibimiz")
    text = models.TextField("Ekip Sayfası Metni", default="Profesyonel ve deneyimli ekibimizle hizmetinizdeyiz.")
    created_at = models.DateTimeField("Tarih", default= timezone.now)
    updated_at = models.DateTimeField("Güncelleme", auto_now=True)
    def __str__(self):
        return self.title


class Employee(models.Model):
    
    hero_image = models.ImageField(upload_to='team_hero/', default='team_hero/default_team_hero.jpg')
    name = models.CharField("Ad", max_length=150)
    position = models.CharField("Pozisyon", max_length=150)
    bio = models.TextField("Açıklama")
    photo = models.ImageField("Fotoğraf", upload_to='employees/')
    order = models.IntegerField("Sıra", default=0)
    page_title = models.CharField("Ekip Sayfası Başlığı", max_length=200,default="Ekibimiz")
    page_text = models.TextField("AEkip Sayfası Metni",default="Profesyonel ve deneyimli ekibimizle hizmetinizdeyiz.")
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']
        verbose_name = "Çalışan"
        verbose_name_plural = "Çalışanlar"


# =========================
# 3. Site İçeriği (Tek kayıt)
# =========================
class SiteContent(models.Model):
    home_title = models.CharField("Ana Sayfa Başlığı", max_length=200)
    home_text = models.TextField("Ana Sayfa Metni")

    about_title = models.CharField("Hakkımızda Başlığı", max_length=200)
    about_text = models.TextField("Hakkımızda Metni")
    
    footer_text = models.TextField("Alt Bilgi (Footer)")

    updated_at = models.DateTimeField("Güncelleme", auto_now=True)
    def __str__(self):
        return "Site İçeriği"

    class Meta:
        verbose_name = "Site İçeriği"
        verbose_name_plural = "Site İçeriği"


from django.db import models
class AboutPage(models.Model):

    # ===== Hero =====
    hero_title = models.CharField(max_length=200)
    hero_text = models.TextField(default="")
    hero_image = models.ImageField(upload_to="about/hero/", blank=True, null=True)
    # ===== Biz Kimiz =====
    about_title = models.CharField(max_length=200)
    about_text = models.TextField(default="")

    # ===== Vision =====
    vision_title = models.CharField(max_length=200,default="")
    vision_text = models.TextField(default="")

    # ===== Mission =====
    mission_title = models.CharField(max_length=200,default="")
    mission_text = models.TextField(default="")

    # ===== Values =====
    values_title = models.CharField(max_length=200,default="")
    values_text = models.TextField(default="")

    # ===== Stats =====
    stat1_number = models.CharField(max_length=20, default="10+")
    stat1_text = models.CharField(max_length=200, default="Yıllık Deneyim")

    stat2_number = models.CharField(max_length=20, default="500+")
    stat2_text = models.CharField(max_length=200, default="Global Müşteri")

    stat3_number = models.CharField(max_length=20, default="1200+")
    stat3_text = models.CharField(max_length=200, default="Tamamlanan Proje")

    stat4_number = models.CharField(max_length=20, default="24/7")
    stat4_text = models.CharField(max_length=200, default="Destek Hizmeti")

    updated_at = models.DateTimeField("Güncelleme", auto_now=True)
    def __str__(self):
        return "Hakkımızda Sayfası"

    class Meta:
        verbose_name = "Hakkımızda"
        verbose_name_plural = "Hakkımızda"

from django.db import models
from django.db import models

class ServicesPage(models.Model):
    hero_title = models.CharField("Başlık (Hero)", max_length=200)
    hero_text = models.TextField("Açıklama (Hero)")
    hero_image = models.ImageField(
        "Görsel (Hero)", 
        upload_to='services/', 
        default='default_services.jpg'
    )
    created_at = models.DateTimeField("Tarih", default= timezone.now)
    updated_at = models.DateTimeField("Güncelleme", auto_now=True)
    def __str__(self):
        return "Hizmet Sayfası"

    class Meta:
        verbose_name = "Hizmet Sayfası"
        verbose_name_plural = "Hizmet Sayfası"


class ServiceArea(models.Model):
    page = models.ForeignKey(
        ServicesPage,
        on_delete=models.CASCADE,
        related_name='areas',
        verbose_name="Sayfa"
    )
    title = models.CharField("Başlık", max_length=200)
    text = models.TextField("Açıklama")
    image = models.ImageField(
        "Görsel",
        upload_to='services/',
        default='default_service.jpg'
    )
    order = models.IntegerField("Sıra", default=0)
    created_at = models.DateTimeField("Tarih", default= timezone.now)
    updated_at = models.DateTimeField("Güncelleme", auto_now=True)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
        verbose_name = "Çalışma Alanı"
        verbose_name_plural = "Çalışma Alanı"
from django.db import models


# =========================
# Blog Page (Hero + Page)
# =========================
class BlogPage(models.Model):
    hero_title = models.CharField("Başlık (Hero)", max_length=200)
    hero_text = models.TextField("Açıklama (Hero)")
    hero_image = models.ImageField(
        "Görsel (Hero)",
        upload_to="blog/",
        default="default_blog.jpg"
    )

    created_at = models.DateTimeField("Tarih", default= timezone.now)
    updated_at = models.DateTimeField("Güncelleme", auto_now=True)
    def __str__(self):
        return "Blog Sayfası"

    class Meta:
        verbose_name = "Blog Sayfası"
        verbose_name_plural = "Blog Sayfası"
print("MODELS LOADED")

# =========================
# Blog Post
# =========================
class BlogPost(models.Model):
    page = models.ForeignKey(
        BlogPage,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Sayfa"
    )

    title = models.CharField("Başlık", max_length=200, null=True, blank=True)
    text = models.TextField("İçerik", null=True, blank=True)
    image = models.ImageField(
        "Görsel",
        upload_to="blog/",
        default="default_post.jpg",
        null=True,
        blank=True
    )

    created_at = models.DateTimeField("Tarih", default= timezone.now)
    updated_at = models.DateTimeField("Güncelleme", auto_now=True)
    order = models.IntegerField("Sıra", default=0)

    def __str__(self):
       # return self.title
        return self.title if self.title else "Adsız Yazı (Başlık Yok)"
    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Blog Yazısı"
        verbose_name_plural = "Blog Yazıları"
from django.db import models

class Karier(models.Model):
    title = models.CharField("Pozisyon Başlığı", max_length=200)
    description = models.TextField("Pozisyon Açıklaması")
    location = models.CharField("Lokasyon", max_length=100, blank=True, null=True)
    posted_date = models.DateField("Yayın Tarihi", auto_now_add=True)
    is_active = models.BooleanField("Aktif", default=True)
    page_title = models.CharField("Sayfa Başlığı", max_length=250, default="Kariyer")
    page_image = models.ImageField("Sayfa Görseli", upload_to="kariyer_images/", blank=True, null=True)
    
    created_at = models.DateTimeField("Tarih", default= timezone.now)
    updated_at = models.DateTimeField("Güncelleme", auto_now=True)
    class Meta:
        verbose_name = "İş İlanı"
        verbose_name_plural = "İş İlanları"
        ordering = ['-posted_date']  # En yeni ilanlar önce

    def __str__(self):
        return self.title
    
from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from django.contrib import admin
from .models import CompanyInfo, Employee, SiteContent, TeamPage


# Company Info (سجل واحد)
@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not CompanyInfo.objects.exists()


# Site Content (سجل واحد)
@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SiteContent.objects.exists()


# Employees
'''
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'order')
    ordering = ('order',)
'''  
'''
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'order', 'photo_thumbnail')
    ordering = ('order',)

    # طريقة لعرض الصورة المصغرة في الـ admin
    def photo_thumbnail(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="width:50px; height:50px; object-fit:cover; border-radius:50%;" />', obj.photo.url)
        return "-"
    photo_thumbnail.short_description = "Fotoğraf"
'''
from django.contrib import admin
from django.utils.html import format_html
from django import forms
from .models import Employee

from django.contrib import admin
from django import forms
from django.utils.html import format_html
from .models import Employee
from PIL import Image


# ================== FORM ==================


class EmployeeAdminForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

        class Media:
            js = ("admin/js/image_preview.js",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # جعل حقول الموظف غير إجبارية داخل Admin فقط
        self.fields["name"].required = False
        self.fields["position"].required = False
        self.fields["bio"].required = False
        self.fields["photo"].required = False
        self.fields["order"].required = False

    def clean(self):
        cleaned_data = super().clean()

        name = cleaned_data.get("name")
        position = cleaned_data.get("position")
        order = cleaned_data.get("order")

        # السماح بحفظ إعدادات الصفحة فقط
        if not name and not position:
            return cleaned_data

        # منع الترتيب أقل من 1
        if order is not None and order < 1:
            self.add_error("order", "الترتيب يجب أن يبدأ من 1")

        # منع تكرار الترتيب
        if order:
            qs = Employee.objects.filter(order=order)
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                self.add_error("order", "هذا الرقم مستخدم بالفعل")

        return cleaned_data


from django.contrib import admin
from django.utils.html import format_html
from PIL import Image
from .models import Employee


from django.contrib import admin
from django.utils.html import format_html

@admin.register(TeamPage)
class TeamPageAdmin(admin.ModelAdmin):
    list_display = ("title", "image_preview")

    fieldsets = (
        ("Page Content", {
            "fields": ("title", "hero_image", "text"),
        }),
    )

    def image_preview(self, obj):
        if obj.hero_image:
            return format_html(
                '<img src="{}" style="width:60px;height:60px;object-fit:cover;border-radius:8px;" />',
                obj.hero_image.url
            )
        return "-"
    image_preview.short_description = "Image"

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeAdminForm

    list_display = ("name", "position", "order", "photo_thumbnail")
    ordering = ("order",)

    fieldsets = (
        ("Employee Info", {
            "fields": ("name", "position", "bio", "photo", "order"),
        }),
    )

    def photo_thumbnail(self, obj):
        if obj.photo and obj.photo.name:
            return format_html(
                '<img src="{}" style="width:50px;height:50px;object-fit:cover;border-radius:50%;" />',
                obj.photo.url
            )
        return "-"
    photo_thumbnail.short_description = "Foto"

    def get_changeform_initial_data(self, request):
        last = Employee.objects.order_by("-order").first()
        if last and last.order:
            return {"order": last.order + 1}
        return {"order": 1}

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        if obj.photo and obj.photo.name:
            try:
                img_path = obj.photo.path
                img = Image.open(img_path)
                img.thumbnail((1200, 1200))
                img = img.convert("RGB")
                img.save(img_path, format="JPEG", quality=85, optimize=True)
            except Exception as e:
                print("Image compression error:", e)

        self.reorder_all()

    def reorder_all(self):
        employees = Employee.objects.order_by("order")

        for index, emp in enumerate(employees, start=1):
            if emp.order != index:
                emp.order = index
                emp.save(update_fields=["order"])

    def has_delete_permission(self, request, obj=None):
        if obj and obj.pk == 1:
            return False
        return True
        
from django.contrib import admin
from .models import AboutPage


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):

    fieldsets = (
        ("Hero Bölümü", {
            "fields": ("hero_title", "hero_text","hero_image"),
        }),

        ("Biz Kimiz", {
            "fields": ("about_title", "about_text"),
        }),

        ("Vizyon", {
            "fields": ("vision_title", "vision_text"),
        }),

        ("Misyon", {
            "fields": ("mission_title", "mission_text"),
        }),

        ("Değerler", {
            "fields": ("values_title", "values_text"),
        }),

        ("İstatistikler", {
            "fields": (
                "stat1_number", "stat1_text",
                "stat2_number", "stat2_text",
                "stat3_number", "stat3_text",
                "stat4_number", "stat4_text",
            ),
        }),
    )

    # Only one page (صفحة hakkimizda واحدة فقط)
    def has_add_permission(self, request):
        return not AboutPage.objects.exists()
from django.contrib import admin
'''
from .models import WorkAreasPage, WorkArea

from django.contrib import admin
from django.utils.html import format_html
from .models import WorkAreasPage, WorkArea

# =========================
# Inline for each WorkArea
# =========================
class WorkAreaInline(admin.TabularInline):
    model = WorkArea
    extra = 1  # عدد الحقول الإضافية التي تظهر عند إضافة جديد
    fields = ('title', 'text', 'image', 'order', 'gorsel_onizleme')
    readonly_fields = ('gorsel_onizleme',)
    ordering = ('order',)
    show_change_link = True  # يسمح بالضغط على المجال للذهاب إلى صفحة تحريره

    # معاينة الصورة في الـ Admin
    def gorsel_onizleme(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width:120px; height:auto; border-radius:5px;"/>', obj.image.url)
        return "(Görsel yok)"
    gorsel_onizleme.short_description = "Önizleme"

# =========================
# Admin لصفحة WorkAreasPage
# =========================
@admin.register(WorkAreasPage)
class WorkAreasPageAdmin(admin.ModelAdmin):
    inlines = [WorkAreaInline]

    fieldsets = (
        ("Hero Bölümü", {
            "fields": ("hero_title", "hero_text", "hero_image"),
        }),
    )

    # يمنع إنشاء أكثر من صفحة واحدة
    def has_add_permission(self, request):
        return not WorkAreasPage.objects.exists()
'''

from django.contrib import admin
from django.utils.html import format_html
from .models import ServicesPage, ServiceArea  # <- الأسماء الجديدة

# =========================
# Inline لكل ServiceArea
# =========================
class ServiceAreaInline(admin.TabularInline):
    model = ServiceArea
    extra = 1
    fields = ('title', 'text', 'image', 'order', 'gorsel_onizleme')
    readonly_fields = ('gorsel_onizleme',)
    ordering = ('order',)
    show_change_link = True

    # معاينة الصورة في الـ Admin
    def gorsel_onizleme(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width:120px; height:auto; border-radius:5px;"/>', obj.image.url)
        return "(Görsel yok)"
    gorsel_onizleme.short_description = "Önizleme"

# =========================
# Admin لصفحة ServicesPage
# =========================
@admin.register(ServicesPage)
class ServicesPageAdmin(admin.ModelAdmin):
    inlines = [ServiceAreaInline]

    fieldsets = (
        ("Hero Bölümü", {
            "fields": ("hero_title", "hero_text", "hero_image"),
        }),
    )

    # يمنع إنشاء أكثر من صفحة واحدة
    def has_add_permission(self, request):
        return not ServicesPage.objects.exists()

from django.contrib import admin
from django.utils.html import format_html
from .models import BlogPage, BlogPost


# Inline للبوستات
class BlogPostInline(admin.TabularInline):
    model = BlogPost
    extra = 1
    fields = ("title", "text", "image", "order", "image_preview")
    readonly_fields = ("image_preview",)
    ordering = ("order",)
    show_change_link = True

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:120px; border-radius:6px;" />',
                obj.image.url
            )
        return "(Görsel yok)"

    image_preview.short_description = "Önizleme"


@admin.register(BlogPage)
class BlogPageAdmin(admin.ModelAdmin):
    inlines = [BlogPostInline]

    fieldsets = (
        ("Hero Bölümü", {
            "fields": ("hero_title", "hero_text", "hero_image"),
        }),
    )

    # صفحة واحدة فقط
    def has_add_permission(self, request):
        return not BlogPage.objects.exists()
from django.contrib import admin
from .models import Karier

@admin.register(Karier)
class KarierAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'posted_date', 'is_active','page_title','page_image')
    list_filter = ('posted_date', 'is_active')
    search_fields = ('title', 'description', 'location')
    list_editable = ('is_active',)
    
    
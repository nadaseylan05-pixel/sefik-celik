from django.shortcuts import render
from .models import CompanyInfo, SiteContent,Employee,AboutPage


# Create your views here.
def home(request):
    company = CompanyInfo.objects.first()
    content = SiteContent.objects.first()
    #employees = Employee.objects.all()

    return render(request, 'index.html', {
        'company': company,
        'content': content,
        #'employees': employees,
    })

def hakimizda(request):
    content =AboutPage.objects.first()
    employee = Employee.objects.all()
    content1 = SiteContent.objects.first()
    employees =Employee.objects.all()
    return render(request, 'hakimizda.html',{
        'content': content,
        'employee': employee,
        'content1': content1,
        'employees':employees,
        
    })
def blog(request):
    return render(request, 'blog.html')
'''
def ekibimiz(request):
    members =Team.objects.all()
    return render(request, 
                    'ekibimiz.html',{'members':members})
'''
def ekibimiz(request):
    teampage=TeamPage.objects.first()
    employees =Employee.objects.all()
    content1 = SiteContent.objects.first()
    return render(request, 'ekibimiz.html',{
        'teampage': teampage,
        'employees': employees,
        'content1': content1,
        })
                   
from .models import ServicesPage, ServiceArea , TeamPage
def work_areas_view(request):
    # جلب أول صفحة WorkAreasPage موجودة
    page = ServicesPage.objects.first()
    content1 = SiteContent.objects.first()
    context = {
        'page': page,
        'content1':content1
    }
    return render(request, 'Çalışma_alanları.html', context)

from django.shortcuts import get_object_or_404
#Last added
'''
def service_area_detail(request, id):
    area = get_object_or_404(ServiceArea, id=id)
    return render(request, "service_area_detail.html", {"area": area})
'''    
from django.shortcuts import render
from .models import BlogPage


def blog(request):
    page = BlogPage.objects.first()
    posts = page.posts.all() if page else []
    content1 = SiteContent.objects.first()
    return render(request, "blog.html", {
        "page": page,
        "posts": posts,
        "content1":content1
    })
#Last added 
'''
from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)
    return render(request, "blog_detail.html", {"post": post})
 '''   
from django.shortcuts import render, get_object_or_404
from .models import BlogPost

# views.py
from django.shortcuts import render
from .models import CompanyInfo, SiteContent

def iletişim(request):
    company = CompanyInfo.objects.first()
    content = SiteContent.objects.first()
    content1 = SiteContent.objects.first()
    return render(request, 'iletişim.html', {
        'company': company,
        'content': content,
        'content1':content1,
    })
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CompanyInfo, SiteContent
'''
def send_message(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # هنا ممكن تحفظ الرسالة في قاعدة بيانات، أو ترسل ايميل
        # مثال سريع للطباعة فقط:
        print(f"New message from {name} ({email}): {message}")

        messages.success(request, "Mesajınız başarıyla gönderildi!")
        return redirect('iletişim')  # ترجع نفس صفحة الاتصال

    return redirect('iletişim') 
'''
from django.shortcuts import render, get_object_or_404
from .models import Karier
from django.shortcuts import render
from .models import Karier

def kariyer(request):
    jobs = Karier.objects.filter(is_active=True)
    page = Karier.objects.first()
    content1 = SiteContent.objects.first()

    return render(request, 'kariyer.html',{
        'jobs': jobs,
        'page': page,
        'content1': content1,
    })

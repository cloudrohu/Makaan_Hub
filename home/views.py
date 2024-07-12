import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Avg, Count, Q, F
from django.db.models.functions import Concat
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import translation

from home.forms import SearchForm
from home.models import Setting, ContactForm, ContactMessage,FAQ,About_Page,Contact_Page,Testimonial,Our_Team
from Makaan_Hub import settings
from utility.models import City,Locality,Residential_Property_Type
from user.models import Developer
from project.models import Commercial_Project_Images,Commercial_Project,Residential_Project,Residential_Project_Images

# Create your views here.


def index(request):
    setting = Setting.objects.all().order_by('-id')[0:1]
    
    city = City.objects.all()
    about = About_Page.objects.all().order_by('-id')[0:1]

    locality = Locality.objects.filter(featured_locality = 'True').order_by('-id')[:18]

    developer = Developer.objects.filter(featured_builder = 'True').order_by('-id')[:50]  #first 4 products
    ourteam = Our_Team.objects.filter(featured = 'True').order_by('-id')#first 4 products
    testimonial = Testimonial.objects.filter(featured = 'True').order_by('-id')#first 4 products
    project_slider = Residential_Project.objects.filter(slider = 'True').order_by('-id')[:6]  #first 4 products
    project_latest = Residential_Project.objects.filter(featured_project = 'True').order_by('-id')[:6]  # last 4 products
    project_featured = Residential_Project.objects.filter(featured_project = 'True').order_by('-id')[:12]  # last 4 products
    project_picked = Residential_Project.objects.filter(featured_project = 'True').order_by('?')[:6]   #Random selected 4 products

    page="home"
    context={
        'setting':setting,
        'city':city,
        'about':about,
        'testimonial':testimonial,
        'ourteam':ourteam,
        'locality':locality,
        'developer':developer,
        'project_slider':project_slider,
        'project_latest':project_latest,
        'project_picked':project_picked,
        'project_featured':project_featured,
    }

    return render(request,'index.html',context)

def residential_project(request):
    setting = Setting.objects.all().order_by('-id')[0:1]
     # last 4 products
    project_picked = Residential_Project.objects.all().order_by('?') #Random selected 4 products
    project_featured = Residential_Project.objects.filter(featured_project = 'True').order_by('-id')[:9]  # last 4 products
    Property_Type = Residential_Property_Type.objects.all().order_by('-id') # last 4 products

    page="home"
    context={
        'setting':setting,
        
        'project_picked':project_picked,
        'project_featured':project_featured,
        'Property_Type':Property_Type,

    }

    return render(request,'projects/residential_list.html',context)


def residential_project_details(request,slug):
    setting = Setting.objects.all().order_by('-id')[0:1]
     # last 4 products

    project_picked = Residential_Project.objects.get(slug = slug)

    page="home"
    context={
        'setting':setting,

        'project_picked':project_picked,

    }

    return render(request,'projects/residential_view.html',context)


def commercial_project(request):
    setting = Setting.objects.all().order_by('-id')[0:1]
    
    city = City.objects.all()
    locality = Locality.objects.all()

    developer = Developer.objects.filter(featured_builder = 'True').order_by('-id')[:50]  #first 4 products
    ourteam = Our_Team.objects.filter(featured = 'True').order_by('-id')#first 4 products
    testimonial = Testimonial.objects.filter(featured = 'True').order_by('-id')#first 4 products
    project_slider = Residential_Project.objects.filter(slider = 'True').order_by('-id')[:6]  #first 4 products
    project_latest = Residential_Project.objects.filter(featured_project = 'True').order_by('-id')[:6]  # last 4 products
    project_featured = Residential_Project.objects.filter(featured_project = 'True').order_by('-id')[:6]  # last 4 products
    project_picked = Residential_Project.objects.filter(featured_project = 'True').order_by('?')[:6]   #Random selected 4 products

    page="home"
    context={
        'setting':setting,
        'city':city,
        'testimonial':testimonial,
        'ourteam':ourteam,
        'locality':locality,
        'developer':developer,
        'project_slider':project_slider,
        'project_latest':project_latest,
        'project_picked':project_picked,
        'project_featured':project_featured,
    }

    return render(request,'projects/commercial_list.html',context)

def land(request):
    setting = Setting.objects.all().order_by('-id')[0:1]
    
    city = City.objects.all()
    locality = Locality.objects.all()

    developer = Developer.objects.filter(featured_builder = 'True').order_by('-id')[:50]  #first 4 products
    ourteam = Our_Team.objects.filter(featured = 'True').order_by('-id')#first 4 products
    testimonial = Testimonial.objects.filter(featured = 'True').order_by('-id')#first 4 products
    project_slider = Residential_Project.objects.filter(slider = 'True').order_by('-id')[:6]  #first 4 products
    project_latest = Residential_Project.objects.filter(featured_project = 'True').order_by('-id')[:6]  # last 4 products
    project_featured = Residential_Project.objects.filter(featured_project = 'True').order_by('-id')[:6]  # last 4 products
    project_picked = Residential_Project.objects.filter(featured_project = 'True').order_by('?')[:6]   #Random selected 4 products

    page="home"
    context={
        'setting':setting,
        'city':city,
        'testimonial':testimonial,
        'ourteam':ourteam,
        'locality':locality,
        'developer':developer,
        'project_slider':project_slider,
        'project_latest':project_latest,
        'project_picked':project_picked,
        'project_featured':project_featured,
    }

    return render(request,'index.html',context)

def pg(request):
    setting = Setting.objects.all().order_by('-id')[0:1]
    
    city = City.objects.all()
    locality = Locality.objects.all()
    about = About_Page.objects.all().order_by('-id')[0:1]


    developer = Developer.objects.filter(featured_builder = 'True').order_by('-id')[:50]  #first 4 products
    ourteam = Our_Team.objects.filter(featured = 'True').order_by('-id')#first 4 products
    testimonial = Testimonial.objects.filter(featured = 'True').order_by('-id')#first 4 products
    project_slider = Residential_Project.objects.filter(slider = 'True').order_by('-id')[:6]  #first 4 products
    project_latest = Residential_Project.objects.filter(featured_project = 'True').order_by('-id')[:6]  # last 4 products
    project_featured = Residential_Project.objects.filter(featured_project = 'True').order_by('-id')[:6]  # last 4 products
    project_picked = Residential_Project.objects.filter(featured_project = 'True').order_by('?')[:6]   #Random selected 4 products

    page="home"
    context={
        'setting':setting,
        'about':about,

        'city':city,
        'testimonial':testimonial,
        'ourteam':ourteam,
        'locality':locality,
        'developer':developer,
        'project_slider':project_slider,
        'project_latest':project_latest,
        'project_picked':project_picked,
        'project_featured':project_featured,
    }

    return render(request,'index.html',context)

def blog(request):
    setting = Setting.objects.all().order_by('-id')[0:1]
    
    city = City.objects.all()
    locality = Locality.objects.all()

    developer = Developer.objects.filter(featured_builder = 'True').order_by('-id')[:50]  #first 4 products
    ourteam = Our_Team.objects.filter(featured = 'True').order_by('-id')#first 4 products
    testimonial = Testimonial.objects.filter(featured = 'True').order_by('-id')#first 4 products
    project_slider = Residential_Project.objects.filter(slider = 'True').order_by('-id')[:6]  #first 4 products
    project_latest = Residential_Project.objects.filter(featured_project = 'True').order_by('-id')[:6]  # last 4 products
    project_featured = Residential_Project.objects.filter(featured_project = 'True').order_by('-id')[:6]  # last 4 products
    project_picked = Residential_Project.objects.filter(featured_project = 'True').order_by('?')[:6]   #Random selected 4 products

    page="home"
    context={
        'setting':setting,
        'city':city,
        'testimonial':testimonial,
        'ourteam':ourteam,
        'locality':locality,
        'developer':developer,
        'project_slider':project_slider,
        'project_latest':project_latest,
        'project_picked':project_picked,
        'project_featured':project_featured,
    }

    return render(request,'index.html',context)


def aboutus(request):
    #category = categoryTree(0,'',currentlang)
    setting = Setting.objects.all().order_by('-id')[0:1]


    about = About_Page.objects.all().order_by('-id')[0:1]

    city = City.objects.all()

    
    context={
        'setting':setting,
        'city':city,
        'about':about,
    }
 
    return render(request, 'about.html',context)

def contactus(request):
    setting = Setting.objects.all().order_by('-id')[0:1]
    
    city = City.objects.all()


    if request.method == 'POST': # check post
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage() #create relation with model
            data.name = form.cleaned_data['name'] # get form input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  #save data to table
            messages.success(request,"Your message has ben sent. Thank you for your message.")
            return HttpResponseRedirect('/contact')
    form = ContactForm
    context={
        'setting':setting,
        'form':form ,
        'city':city,
    }    
    return render(request, 'contactus.html',context)

def category_products(request,id,slug):
    
    city = City.objects.all()

    
    context={
             #'category':category,
             'city':city }
    return render(request,'category_products.html',context)

def search(request):
    if request.method == 'POST': # check post
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query'] # get form input data
            catid = form.cleaned_data['catid']
            if catid==0:
                products=Product.objects.filter(title__icontains=query)  #SELECT * FROM product WHERE title LIKE '%query%'
            else:
                products = Product.objects.filter(title__icontains=query,category_id=catid)

            category = Category.objects.all()
            context = {'products': products,
                        'query':query,
                       'category': category }
            return render(request, 'search_products.html', context)

    return HttpResponseRedirect('/')

def search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        projects = Project.objects.filter(title__icontains=q)

        results = []
        for rs in projects:
            project_json = {}
            project_json = rs.title +" > " + rs.locality.title
            results.append(project_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'

    return HttpResponse(data, mimetype)

def project_detail(request,id,slug):
    query = request.GET.get('q')
    # >>>>>>>>>>>>>>>> M U L T I   L A N G U G A E >>>>>> START
    #defaultlang = settings.LANGUAGE_CODE[0:2] #en-EN
    #currentlang = request.LANGUAGE_CODE[0:2]
    #category = categoryTree(0, '', currentlang)
    city = City.objects.all()

    project = Project.objects.get(pk=id)

    
    # <<<<<<<<<< M U L T I   L A N G U G A E <<<<<<<<<<<<<<< end

    images = Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id,status='True')
    context = {'project': project,'city': city,
               'images': images, 'comments': comments,
               }
    
    return render(request,'product_detail1.html',context)

def faq(request):
   
    return render(request, 'faq.html')

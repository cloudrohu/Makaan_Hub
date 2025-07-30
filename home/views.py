import json
import django_filters

from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Avg, Count, Q, F
from django.db.models.functions import Concat
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.shortcuts import redirect, render
from django.core.mail import send_mail

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import translation
from django.shortcuts import render, get_object_or_404
from home.forms import ResidentialEnquiryForm, CommercialEnquiryForm
from .filters import ResidentialFilter
from home.models import Setting, ContactForm, ContactMessage,FAQ,About_Page,Contact_Page,Testimonial,Our_Team,Slider
from utility.models import City,Locality
from django.db.models import Q
from user.models import Developer
from project.models import Residential,CommercialProject
from home.filters import ResidentialFilter

# Create your views here.


def index(request):
    setting = Setting.objects.all().order_by('-id')[0:1]
    city = City.objects.all()
    about = About_Page.objects.all().order_by('-id')[0:1]
    slider = Slider.objects.filter(featured_project='True').order_by('?')[:9]
    project_featured = Residential.objects.filter(featured_property='True').order_by('-id')[:9]
    commercia_featured = CommercialProject.objects.filter(featured_property='True').order_by('-id')[:9]
    featured_locality = Locality.objects.filter(featured_locality='True').order_by('-id')[:9]
    developer = Developer.objects.filter(featured_builder='True').order_by('-id')[:50]
    ourteam = Our_Team.objects.filter(featured='True').order_by('-id')
    testimonial = Testimonial.objects.filter(featured='True').order_by('-id')

    query = request.GET.get('q')
    residential_search = Residential.objects.filter(active=True)
    commercial_search = CommercialProject.objects.filter(active=True)

    if query:
        residential_search = residential_search.filter(
            Q(project_name__icontains=query) | Q(locality__title__icontains=query)
        )
        commercial_search = commercial_search.filter(
            Q(project_name__icontains=query) | Q(locality__title__icontains=query)
        )

    context = {
        'project_featured': project_featured,
        'setting': setting,
        'city': city,
        'about': about,
        'slider': slider,
        'testimonial': testimonial,
        'ourteam': ourteam,
        'developer': developer,
        'commercia_featured': commercia_featured,
        'featured_locality': featured_locality,
        'query': query,  # search box me value dikhane ke liye
        'residential_search': residential_search,
        'commercial_search': commercial_search,
    }

    return render(request, 'index.html', context)

from django.db.models import Q

def residential_project(request):
    setting = Setting.objects.all().order_by('-id')[0:1]
    project_featured = Residential.objects.filter(featured_property=True).order_by('?')[:6]

    all_active = Residential.objects.filter(active=True)

    # 🧠 Keyword search logic
    query = request.GET.get('q', '')
    if query:
        all_active = all_active.filter(
            Q(project_name__icontains=query) |
            Q(locality__title__icontains=query) |
            Q(headers__keywords__icontains=query)
        ).distinct()

    # 🧠 Filter apply karo (aapka existing ResidentialFilter)
    residential_filter = ResidentialFilter(request.GET, queryset=all_active)
    filtered_qs = residential_filter.qs


    paginator = Paginator(filtered_qs, 20)  # 20 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'project_featured': project_featured,
        'active': page_obj,
        'setting': setting,
        'filter': residential_filter,
        'query': query,
    }
    return render(request, 'projects/list/residential.html', context)


def residential_project_details(request, slug):
    setting = Setting.objects.all().order_by('-id')[:1]
    project = get_object_or_404(Residential, slug=slug)

    # Optional: related projects, developer projects, etc.
    related_projects = Residential.objects.filter(city=project.city).exclude(slug=slug).order_by('?')[:3]

    context = {
        'setting': setting,
        'active': project,
        'related_projects': related_projects,
        'page': 'home'
    }
    return render(request, 'projects/details/residential.html', context)


def commercial_project(request):
    setting = Setting.objects.all().order_by('-id')[:1]

    project_featured = CommercialProject.objects.filter(featured_property=True).order_by('?')[:6]

    all_active = CommercialProject.objects.filter(active=True)

    # 🧠 Keyword search logic
    query = request.GET.get('q', '')
    if query:
        all_active = all_active.filter(
            Q(project_name__icontains=query) |
            Q(locality__title__icontains=query) |
            Q(headers__keywords__icontains=query)
        ).distinct()

    # 🧠 Apply filter (agar aapke paas CommercialFilter hai toh use karo)
    commercial_filter = ResidentialFilter(request.GET, queryset=all_active)  # ideally CommercialFilter use karo
    filtered_qs = commercial_filter.qs

    paginator = Paginator(filtered_qs, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'project_featured': project_featured,
        'active': page_obj,
        'setting': setting,
        'filter': commercial_filter,
        'page': 'home',
        'query': query,  # template me search box me value dikhane ke liye
    }

    return render(request, 'projects/list/commercial.html', context)


def commercial_project_details(request,slug):
    setting = Setting.objects.all().order_by('-id')[0:1]
     # last 4 products
    active = get_object_or_404(CommercialProject, slug=slug)


    page="home"
    context={
        'setting':setting,
        'active':active,

    }
    return render(request,'projects/details/commercial.html',context)


def land(request):
    setting = Setting.objects.all().order_by('-id')[0:1]
    
    city = City.objects.all()
    locality = Locality.objects.all()

    developer = Developer.objects.filter(featured_builder = 'True').order_by('-id')[:50]  #first 4 products
    ourteam = Our_Team.objects.filter(featured = 'True').order_by('-id')#first 4 products
    testimonial = Testimonial.objects.filter(featured = 'True').order_by('-id')#first 4 products
    project_latest = Residential.objects.filter(featured_project = 'True').order_by('-id')[:6]  # last 4 products
    project_featured = Residential.objects.filter(featured_project = 'True').order_by('-id')[:6]  # last 4 products
    project_picked = Residential.objects.filter(featured_project = 'True').order_by('?')[:6]   #Random selected 4 products

    page="home"
    context={
        'setting':setting,
        'city':city,
        'testimonial':testimonial,
        'ourteam':ourteam,
        'locality':locality,
        'developer':developer,
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
    project_slider = Residential.objects.filter(slider = 'True').order_by('-id')[:6]  #first 4 products
    project_latest = Residential.objects.filter(featured_project = 'True').order_by('-id')[:6]  # last 4 products
    project_featured = Residential.objects.filter(featured_project = 'True').order_by('-id')[:6]  # last 4 products
    project_picked = Residential.objects.filter(featured_project = 'True').order_by('?')[:6]   #Random selected 4 products

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
    project_slider = Residential.objects.filter(slider = 'True').order_by('-id')[:6]  #first 4 products
    project_latest = Residential.objects.filter(featured_project = 'True').order_by('-id')[:6]  # last 4 products
    project_featured = Residential.objects.filter(featured_project = 'True').order_by('-id')[:6]  # last 4 products
    project_picked = Residential.objects.filter(featured_project = 'True').order_by('?')[:6]   #Random selected 4 products

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

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.ip = request.META.get('REMOTE_ADDR')
            contact.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('thank-you')
    else:
        form = ContactForm()

    context = {
        'form': form,
        'setting': setting,
        'city': city,
    }
    return render(request, 'contactus.html', context)


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


def privacy_policy(request): 
    header = Setting.objects.all().order_by('-id')[0:1]  

    context={
        'header':header,
    }
    return render(request,'privacy-policy.html',context)



def THANK_YOU(request):
    return render(request, 'thank-you.html')


def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('mobile')
        

         # Save to DB
        Response.objects.create(name=name, email=email, phone=phone)

        # Send "Thank You" email to user
        subject = 'Thank You for Contacting '
        message = f"""
Dear {name},

Thank you for Connecting. We have received your details:

Email: {email}  
Phone: {phone}

Our team will contact you shortly.

Kind regards 
All the best
"""
        from_email = None  # Uses DEFAULT_FROM_EMAIL in settings.py
        recipient_list = [email]  # ← Send to user, not to admin

        try:
            send_mail(subject, message, from_email, recipient_list)
        except Exception as e:
            print("Error sending email:", e)
        return redirect('thank_you')  # Make sure this name matches urls.py

    return render(request, 'base.html')


def submit_enquiry(request, pk):
    residential = get_object_or_404(Residential, pk=pk)
    if request.method == 'POST':
        form = ResidentialEnquiryForm(request.POST)
        if form.is_valid():
            enquiry = form.save(commit=False)
            enquiry.residential = residential
            enquiry.save()

            # ✅ Admin ko email
            send_mail(
                subject=f"New Enquiry for {residential.project_name}",
                message=(
                    f"Name: {enquiry.name}\n"
                    f"Phone: {enquiry.phone}\n"
                    f"Email: {enquiry.email}\n"
                    f"Message: {enquiry.message}"
                ),
                from_email=None,
                recipient_list=['admin@example.com'],
                fail_silently=False,
            )

            # ✅ User ko confirmation email
            if enquiry.email:
                send_mail(
                    subject="Thanks for your enquiry!",
                    message=(
                        f"Dear {enquiry.name},\n\n"
                        f"Thank you for enquiring about {residential.project_name}.\n"
                        f"Our team will get back to you soon.\n\n"
                        f"Regards,\nMakaanHub Team"
                    ),
                    from_email=None,
                    recipient_list=[enquiry.email],
                    fail_silently=False,
                )

            return redirect('/thank-you/')  # 🔥 thank-you page
    else:
        form = ResidentialEnquiryForm()
    return render(request, 'partials/enquiry_form.html', {'form': form})

def submit_commercial_enquiry(request, pk):
    commercial = get_object_or_404(CommercialProject, pk=pk)

    if request.method == 'POST':
        form = CommercialEnquiryForm(request.POST)
        if form.is_valid():
            enquiry = form.save(commit=False)
            enquiry.commercial = commercial
            enquiry.save()

            # ✅ Admin ko email
            send_mail(
                subject=f"New Enquiry for {commercial.project_name}",
                message=(
                    f"Name: {enquiry.name}\n"
                    f"Phone: {enquiry.phone}\n"
                    f"Email: {enquiry.email}\n"
                    f"Message: {enquiry.message}"
                ),
                from_email=None,
                recipient_list=['admin@example.com'],  # ⚠️ Replace with real email
                fail_silently=False,
            )

            # ✅ User ko confirmation email
            if enquiry.email:
                send_mail(
                    subject="Thanks for your enquiry!",
                    message=(
                        f"Dear {enquiry.name},\n\n"
                        f"Thank you for enquiring about {commercial.project_name}.\n"
                        f"Our team will get back to you soon.\n\n"
                        f"Regards,\nMakaanHub Team"
                    ),
                    from_email=None,
                    recipient_list=[enquiry.email],
                    fail_silently=False,
                )

            return redirect('/thank-you/')  # ✅ Redirect to Thank You
    else:
        form = CommercialEnquiryForm()

    return render(request, 'partials/enquiry_form.html', {'form': form})


class ResidentialFilter(django_filters.FilterSet):
    locality = django_filters.CharFilter(lookup_expr='icontains', label='Locality')
    propert_type = django_filters.CharFilter(lookup_expr='icontains', label='Property Type')
    bhk = django_filters.CharFilter(lookup_expr='iexact', label='BHK')

    class Meta:
        model = Residential
        fields = ['locality', 'propert_type', 'bhk']

    
import json
import django_filters
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Avg, Count, Q, F
from django.db.models.functions import Concat
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.core.mail import send_mail

from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/calendar']

from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import translation
from home.forms import ResidentialEnquiryForm, CommercialEnquiryForm
from home.filters import ResidentialFilter
from home.models import Setting, ContactForm, ContactMessage, FAQ, About_Page, Contact_Page, Testimonial, Our_Team, Slider
from utility.models import City, Locality
from user.models import Developer
from project.models import Residential, CommercialProject
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch


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
        'query': query,
        'residential_search': residential_search,
        'commercial_search': commercial_search,
    }

    return render(request, 'index.html', context)


def residential_project(request):
    setting = Setting.objects.all().order_by('-id')[0:1]
    project_featured = Residential.objects.filter(featured_property=True).order_by('?')[:9]

    all_active = Residential.objects.filter(active=True)

    query = request.GET.get('q', '')
    if query:
        all_active = all_active.filter(
            Q(project_name__icontains=query) |
            Q(locality__title__icontains=query) |
            Q(headers__keywords__icontains=query)
        ).distinct()

    residential_filter = ResidentialFilter(request.GET, queryset=all_active)
    filtered_qs = residential_filter.qs

    paginator = Paginator(filtered_qs, 20)
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


def residential_project_details(request, id, slug):
    setting = Setting.objects.all().order_by('-id')[:1]
    project = get_object_or_404(Residential, id=id, slug=slug)

    related_projects = Residential.objects.filter(city=project.city).exclude(id=id).order_by('?')[:3]

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

    query = request.GET.get('q', '')
    if query:
        all_active = all_active.filter(
            Q(project_name__icontains=query) |
            Q(locality__title__icontains=query) |
            Q(headers__keywords__icontains=query)
        ).distinct()

    # NOTE: ideally use a CommercialFilter if available
    commercial_filter = ResidentialFilter(request.GET, queryset=all_active)
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
        'query': query,
    }

    return render(request, 'projects/list/commercial.html', context)


def commercial_project_details(request, slug):
    setting = Setting.objects.all().order_by('-id')[0:1]
    active = get_object_or_404(CommercialProject, slug=slug)

    context = {
        'setting': setting,
        'active': active,
    }
    return render(request, 'projects/details/commercial.html', context)


def land(request):
    setting = Setting.objects.all().order_by('-id')[0:1]
    city = City.objects.all()
    locality = Locality.objects.all()

    developer = Developer.objects.filter(featured_builder='True').order_by('-id')[:50]
    ourteam = Our_Team.objects.filter(featured='True').order_by('-id')
    testimonial = Testimonial.objects.filter(featured='True').order_by('-id')
    project_latest = Residential.objects.filter(featured_project='True').order_by('-id')[:6]
    project_featured = Residential.objects.filter(featured_project='True').order_by('-id')[:6]
    project_picked = Residential.objects.filter(featured_project='True').order_by('?')[:6]

    context = {
        'setting': setting,
        'city': city,
        'testimonial': testimonial,
        'ourteam': ourteam,
        'locality': locality,
        'developer': developer,
        'project_latest': project_latest,
        'project_picked': project_picked,
        'project_featured': project_featured,
    }

    return render(request, 'index.html', context)


def pg(request):
    setting = Setting.objects.all().order_by('-id')[0:1]
    city = City.objects.all()
    locality = Locality.objects.all()
    about = About_Page.objects.all().order_by('-id')[0:1]

    developer = Developer.objects.filter(featured_builder='True').order_by('-id')[:50]
    ourteam = Our_Team.objects.filter(featured='True').order_by('-id')
    testimonial = Testimonial.objects.filter(featured='True').order_by('-id')
    project_slider = Residential.objects.filter(slider='True').order_by('-id')[:6]
    project_latest = Residential.objects.filter(featured_project='True').order_by('-id')[:6]
    project_featured = Residential.objects.filter(featured_project='True').order_by('-id')[:6]
    project_picked = Residential.objects.filter(featured_project='True').order_by('?')[:6]

    context = {
        'setting': setting,
        'about': about,
        'city': city,
        'testimonial': testimonial,
        'ourteam': ourteam,
        'locality': locality,
        'developer': developer,
        'project_slider': project_slider,
        'project_latest': project_latest,
        'project_picked': project_picked,
        'project_featured': project_featured,
    }

    return render(request, 'index.html', context)


def blog(request):
    setting = Setting.objects.all().order_by('-id')[0:1]
    city = City.objects.all()
    locality = Locality.objects.all()

    developer = Developer.objects.filter(featured_builder='True').order_by('-id')[:50]
    ourteam = Our_Team.objects.filter(featured='True').order_by('-id')
    testimonial = Testimonial.objects.filter(featured='True').order_by('-id')
    project_slider = Residential.objects.filter(slider='True').order_by('-id')[:6]
    project_latest = Residential.objects.filter(featured_project='True').order_by('-id')[:6]
    project_featured = Residential.objects.filter(featured_project='True').order_by('-id')[:6]
    project_picked = Residential.objects.filter(featured_project='True').order_by('?')[:6]

    context = {
        'setting': setting,
        'city': city,
        'testimonial': testimonial,
        'ourteam': ourteam,
        'locality': locality,
        'developer': developer,
        'project_slider': project_slider,
        'project_latest': project_latest,
        'project_picked': project_picked,
        'project_featured': project_featured,
    }

    return render(request, 'index.html', context)


def aboutus(request):
    setting = Setting.objects.all().order_by('-id')[0:1]
    about = About_Page.objects.all().order_by('-id')[0:1]
    city = City.objects.all()

    context = {
        'setting': setting,
        'city': city,
        'about': about,
    }

    return render(request, 'about.html', context)


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


def category_products(request, id, slug):
    city = City.objects.all()
    context = {'city': city}
    return render(request, 'category_products.html', context)


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']
            if catid == 0:
                products = Product.objects.filter(title__icontains=query)
            else:
                products = Product.objects.filter(title__icontains=query, category_id=catid)

            category = Category.objects.all()
            context = {'products': products, 'query': query, 'category': category}
            return render(request, 'search_products.html', context)

    return HttpResponseRedirect('/')


def search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        projects = Project.objects.filter(title__icontains=q)

        results = []
        for rs in projects:
            project_json = rs.title + " > " + rs.locality.title
            results.append(project_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def project_detail(request, id, slug):
    city = City.objects.all()
    project = Project.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id, status='True')
    context = {'project': project, 'city': city, 'images': images, 'comments': comments}
    return render(request, 'product_detail1.html', context)


def faq(request):
    return render(request, 'faq.html')


def privacy_policy(request):
    header = Setting.objects.all().order_by('-id')[0:1]
    context = {'header': header}
    return render(request, 'privacy-policy.html', context)


def THANK_YOU(request):
    return render(request, 'thank-you.html')


def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('mobile')

        Response.objects.create(name=name, email=email, phone=phone)

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
        from_email = None
        recipient_list = [email]

        try:
            send_mail(subject, message, from_email, recipient_list)
        except Exception as e:
            print("Error sending email:", e)
        return redirect('thank_you')

    return render(request, 'base.html')


def submit_enquiry(request, pk):
    residential = get_object_or_404(Residential, pk=pk)
    if request.method == 'POST':
        form = ResidentialEnquiryForm(request.POST)
        if form.is_valid():
            enquiry = form.save(commit=False)
            enquiry.residential = residential
            enquiry.save()

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

            return redirect('/thank-you/')
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

            send_mail(
                subject=f"New Enquiry for {commercial.project_name}",
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

            return redirect('/thank-you/')
    else:
        form = CommercialEnquiryForm()

    return render(request, 'partials/enquiry_form.html', {'form': form})


def generate_hindi_pdf(request):
    from io import BytesIO
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    y = height - inch

    p.setFont("Helvetica", 12)
    p.drawString(100, y, "यह एक सैंपल PDF है।")
    p.showPage()
    p.save()

    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')


# Step 1: OAuth start
def google_calendar_init(request):
    flow = Flow.from_client_secrets_file(
        'client_secret.json',
        scopes=SCOPES
    )
    flow.redirect_uri = 'http://127.0.0.1:8000/rest/v1/calendar/redirect/'

    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true'
    )
    request.session['state'] = state
    return HttpResponseRedirect(authorization_url)


# Step 2: OAuth callback
def google_calendar_redirect(request):
    state = request.session.get('state')

    flow = Flow.from_client_secrets_file(
        'client_secret.json',
        scopes=SCOPES,
        state=state
    )
    flow.redirect_uri = 'http://127.0.0.1:8000/rest/v1/calendar/redirect/'
    authorization_response = request.build_absolute_uri()
    flow.fetch_token(authorization_response=authorization_response)

    credentials = flow.credentials

    with open('token.json', 'w') as token:
        token.write(credentials.to_json())

    return HttpResponseRedirect('/')


def search(request):
    query = request.GET.get("q", "")
    category = request.GET.get("category", "")
    sub_category = request.GET.get("sub_category", "")

    residential_results = Residential.objects.filter(active=True)
    commercial_results = CommercialProject.objects.filter(active=True)

    # search filter
    if query:
        residential_results = residential_results.filter(
            Q(project_name__icontains=query) |
            Q(locality__title__icontains=query) |
            Q(city__title__icontains=query) |
            Q(propert_type__icontains=query) |
            Q(construction_status__icontains=query)
        )
        commercial_results = commercial_results.filter(
            Q(project_name__icontains=query) |
            Q(locality__title__icontains=query) |
            Q(city__title__icontains=query) |
            Q(property_type__icontains=query) |
            Q(construction_status__icontains=query)
        )

    # Category based filtering
    if category == "residential":
        commercial_results = CommercialProject.objects.none()

    elif category == "commercial":
        residential_results = Residential.objects.none()

    elif category == "new":
        if sub_category == "residential":
            residential_results = residential_results.filter(construction_status__in=["New Launch", "Under Construction"])
            commercial_results = CommercialProject.objects.none()
        elif sub_category == "commercial":
            commercial_results = commercial_results.filter(construction_status__in=["New Launch", "Under Construction"])
            residential_results = Residential.objects.none()

    context = {
        "query": query,
        "category": category,
        "sub_category": sub_category,
        "residential_results": residential_results,
        "commercial_results": commercial_results,
    }
    return render(request, "projects/search_results.html", context)


def suggestions_api(request):
    q = request.GET.get("q", "").strip()
    category = request.GET.get("category", "")
    suggestions = []

    if len(q) >= 2:
        # City search
        for city in City.objects.filter(title__icontains=q)[:5]:
            suggestions.append({
                "name": city.title,
                "locality": "",
                "city": city.title,
                "type": "City",
                "url": f"/search/?q={city.title}&category={category}"
            })

        # Locality search
        for loc in Locality.objects.filter(title__icontains=q)[:5]:
            suggestions.append({
                "name": loc.title,
                "locality": loc.title,
                "city": loc.city.title if loc.city else "",
                "type": "Locality",
                "url": f"/search/?q={loc.title}&category={category}"
            })

        # Residential projects
        for proj in Residential.objects.filter(project_name__icontains=q, active=True)[:5]:
            suggestions.append({
                "name": proj.project_name,
                "locality": proj.locality.title if proj.locality else "",
                "city": proj.city.title if proj.city else "",
                "type": "Residential Project",
                "url": proj.get_absolute_url()
            })

        # Commercial projects
        for proj in CommercialProject.objects.filter(project_name__icontains=q, active=True)[:5]:
            suggestions.append({
                "name": proj.project_name,
                "locality": proj.locality.title if proj.locality else "",
                "city": proj.city.title if proj.city else "",
                "type": "Commercial Project",
                "url": f"/commercial/{proj.slug}/"
            })

    return JsonResponse(suggestions, safe=False)
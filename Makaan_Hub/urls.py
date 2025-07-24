
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import home
from home import views 
from django.utils.translation import gettext_lazy as _

from django.views.generic import RedirectView

urlpatterns = [


    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('logout/',RedirectView.as_view(url = '/admin/logout/')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path(('about/'), views.aboutus, name='aboutus'),
    path(('contact/'), views.contactus, name='contactus'),
    path('thank-you/', views.THANK_YOU, name='thank-you'),
    path(('residential_project/'), views.residential_project, name='residential_project'),
    path(('residential_project/<slug:slug>'), views.residential_project_details, name='residential_project'),


    path(('commercial_project/'), views.commercial_project, name='commercial_project'),
    path('commercial_project/<slug:slug>/', views.commercial_project_details, name="commercial_project_details"),  # ✅ COMMA IS HERE
    path('submit-commercial-enquiry/<int:pk>/', views.submit_commercial_enquiry, name="submit_commercial_enquiry"),



    path(('land/'), views.land, name='land'),
    path(('pg/'), views.pg, name='pg'),
    path(('blog/'), views.blog, name='blog'),   
    path('category/<int:id>/<slug:slug>', views.category_products, name='category_products'),
    path('privacy-policy', views.privacy_policy, name='privacy-policy'),
    path('enquiry/<int:pk>/', views.submit_enquiry, name='submit_enquiry'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

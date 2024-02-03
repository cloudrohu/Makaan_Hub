
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import home
from home import views 
from django.utils.translation import gettext_lazy as _


urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),



    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),


    path(('about/'), views.aboutus, name='aboutus'),
    path(('contact/'), views.contactus, name='contactus'),

    path(('residential/'), views.residential, name='residential'),
    path(('commercial/'), views.commercial, name='commercial'),
    path(('land/'), views.land, name='land'),
    path(('pg/'), views.pg, name='pg'),
    path(('blog/'), views.blog, name='blog'),



    
    

    path('category/<int:id>/<slug:slug>', views.category_products, name='category_products'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

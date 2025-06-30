from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.utils.html import mark_safe
# Create your models here.
from django.db.models import Avg, Count
from django.forms import ModelForm
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.utils.text import slugify
from utility.models import City,Locality,P_Amenities
from multiselectfield import MultiSelectField
from user.models import Developer


class Residential(MPTTModel):    
    Construction_Status = (
        ('Under Construction', 'Under Construction'),
        ('New Launch', 'New Launch'),
        ('Partially Ready To Move', 'Partially Ready To Move'),
        ('Ready To Move', 'Ready To Move'),
        ('Deleverd', 'Deleverd'),
    )
    Possession_In = (        
        ('2000', '2000'),
        ('2001', '2001'),
        ('2002', '2002'),
        ('2003', '2003'),
        ('2004', '2004'),
        ('2005', '2005'),
        ('2006', '2006'),
        ('2007', '2007'),
        ('2008', '2008'),
        ('2009', '2009'),
        ('2010', '2010'),
        ('2011', '2011'),
        ('2012', '2012'),
        ('2013', '2013'),
        ('2014', '2014'),
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
        ('2022', '2022'),
        ('2023', '2023'),
        ('2024', '2024'),
        ('2025', '2025'),
        ('2026', '2026'),
        ('2027', '2027'),
        ('2028', '2028'),
        ('2029', '2029'),
        ('2030', '2030'),
        ('2031', '2031'),
        ('2032', '2032'),
        ('2033', '2033'),
        ('2034', '2034'),
        ('2035', '2035'),
        ('2036', '2036'),
        ('2037', '2037'),
        ('2038', '2038'),
        ('2039', '2039'),         
 )


    Property_Type = (
        ('1 RK Studio Apartment', '1 RK Studio Apartment'),
        ('Agricultural Farm Land', 'Agricultural Farm Land'),
        ('Farm House', 'Farm House'),
        ('Independent Builder Floor', 'Independent House Villa'),
        ('Residential Apartment', 'Residential Apartment'),
    )
    
    Occupancy_Certificate = (('Yes', 'Yes'),('No', 'No'), )
    Commencement_Certificate = (('Yes', 'Yes'),('No', 'No'),)

    Occupancy_Certificate = models.CharField(max_length=25, choices=Occupancy_Certificate,null=True, blank=True)
    Commencement_Certificate = models.CharField(max_length=25, choices=Commencement_Certificate,null=True, blank=True)
   
    construction_status = models.CharField(max_length=25, choices=Construction_Status)
    propert_type = models.CharField(max_length=200, choices=Property_Type)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    project_name = models.CharField(max_length=250)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)  # many to one relation with Brand
    city = models.ForeignKey(City, on_delete=models.CASCADE)  # many to one relation with Brand
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE)  # many to one relation with Brand

    possession_year = models.CharField(max_length=200, choices=Possession_In,null=True, blank=True)

    Possession = models.CharField(max_length=50)
    land_parceland = models.CharField(max_length=50)
    floor = models.CharField(max_length=50)

    description = models.CharField(max_length=150,null=True, blank=True)
    price = models.CharField(max_length=150,null=True, blank=True)
    image = models.ImageField(null=True, blank=True,upload_to='images/')


    
    def __str__(self):
        return self.project_name
    
    class Meta:
        verbose_name_plural='1. Residential Project'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.project_name + ' ' + self.locality.title + ' ' + self.city.title)
        super(Residential, self).save(*args, **kwargs)

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    class MPTTMeta:
        order_insertion_by = ['project_name']

    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("project_name", kwargs={'slug': self.slug})

    def __str__(self):  # __str__ method elaborated later in
        full_path = [self.project_name]  # post.  use __unicode__ in place of
        k = self.parent
        while k is not None:
            full_path.append(k.project_name)
            k = k.parent
        return ' / '.join(full_path[::-1])

class BookingOffer(models.Model):
    residential = models.ForeignKey(Residential, on_delete=models.CASCADE, related_name="BookingOffer")
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class WelcomeTo(models.Model):
    residential = models.ForeignKey(Residential, on_delete=models.CASCADE, related_name="welcomes")
    description = models.TextField(null=True, blank=True,max_length=5500)
    read_more= models.TextField(null=True, blank=True,max_length=5500)

    def __str__(self):
        return self.description

class Location(models.Model):
    residential = models.ForeignKey(Residential, on_delete=models.CASCADE, related_name="locations")
    google_map_iframe = models.TextField(null=True, blank=True,)

    def __str__(self):
        return self.google_map_iframe

class WebSlider(models.Model):
    residential = models.ForeignKey(Residential, on_delete=models.CASCADE, related_name="sliders")
    image = models.ImageField(upload_to='web_slider/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.caption or f"Slider #{self.pk}"

class Overview(models.Model):
    residential = models.ForeignKey(Residential, on_delete=models.CASCADE, related_name="overviews")
    heading = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.heading

class AboutUs(models.Model):
    residential = models.ForeignKey(Residential, on_delete=models.CASCADE, related_name="aboutus")
    content = models.TextField()

    def __str__(self):
        return "About Us"

class USP(models.Model):
    residential = models.ForeignKey(Residential, on_delete=models.CASCADE, related_name="usps")
    point = models.CharField(null=True, blank=True,max_length=150)
    def __str__(self):
        return self.point

class Configuration(models.Model):
    residential = models.ForeignKey("Residential", on_delete=models.CASCADE, related_name="configurations")
    bhk_type = models.CharField(max_length=50)
    area = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.bhk_type} – {self.area}"

class Connectivity(models.Model):
    residential = models.ForeignKey(Residential, on_delete=models.CASCADE, related_name="configs")
    title = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.title}"

class Project_Amenities(models.Model):
    residential = models.ForeignKey(Residential, on_delete=models.CASCADE, related_name="amenities")
    amenities = models.ForeignKey(P_Amenities, on_delete=models.CASCADE, related_name="amenities")
    
    def __str__(self):
        return f"{self.residential.name} - {self.amenities.name}"

class Gallery(models.Model):
    residential = models.ForeignKey(Residential, on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.caption or f"Image #{self.pk}"

class Header(models.Model):
    residential = models.ForeignKey(Residential, on_delete=models.CASCADE, related_name="headers")    
    keywords = models.CharField(max_length=255,null=True, blank=True)
    meta_description = models.CharField(max_length=255,null=True, blank=True)

    welcome_to_bg = models.ImageField(null=True, blank=True,upload_to='headers/')
    virtual_site_visit_bg = models.ImageField(null=True, blank=True,upload_to='headers/')
    schedule_a_site_visit = models.ImageField(null=True, blank=True,upload_to='headers/')

    def __str__(self):
        return self.keywords

class RERA_Info(models.Model):
    residential = models.ForeignKey(Residential, on_delete=models.CASCADE, related_name="rera")
    qr_image = models.ImageField(null=True, blank=True,upload_to='overviewimage/')
    registration_no= models.CharField(null=True, blank=True,max_length=50)
    project_registered = models.CharField(null=True, blank=True,max_length=50)
    government_rera_authorised_advertiser = models.CharField(null=True, blank=True,max_length=150)
    site_address  = models.CharField(null=True, blank=True,max_length=500)
    contact_us= models.CharField(null=True, blank=True,max_length=500)
    disclaimer= models.CharField(null=True, blank=True,max_length=1500)
    document = models.FileField(null=True, blank=True,upload_to='rera_docs/')

    def __str__(self):
        return self.registration_no

class WhyInvest(models.Model):
    residential = models.ForeignKey(Residential, on_delete=models.CASCADE, related_name="why_invest")
    title = models.CharField(max_length=350,null=True, blank=True)
    discripation = models.CharField(max_length=500,null=True, blank=True)
    

    def __str__(self):
        return f"Why Invest - {self.pk}"
    

class BookingOffer(models.Model):
    residential = models.ForeignKey('Residential', on_delete=models.CASCADE, related_name="booking_offers")
    bank_approval = models.ForeignKey('utility.Bank', on_delete=models.CASCADE, related_name='booking_offers')
    title = models.CharField(max_length=200,null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    
#__________________________________________________________________________________________________________
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

# Residential Projects Start Here #

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

    land_parce = models.CharField(max_length=50,null=True, blank=True)
    floor = models.CharField(max_length=50,null=True, blank=True)
    possession = models.CharField(max_length=50,null=True, blank=True)
    possession_year = models.CharField(max_length=200, choices=Possession_In,null=True, blank=True)
    luxurious = models.CharField(max_length=50,null=True, blank=True)
    priceing = models.CharField(max_length=50,null=True, blank=True)    

    featured_property = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True,upload_to='images/')

    slug = models.SlugField(unique=True, null=True, blank=True,max_length=555,)
    create_at = models.DateTimeField(auto_now_add=True,null=True, blank=True,)
    update_at = models.DateTimeField(auto_now=True,null=True, blank=True,)
    
    def __str__(self):
        return str(self.project_name) if self.project_name else "Unnamed Project"
    
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
        return reverse("residential_project", kwargs={'slug': self.slug})

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
        return f"{self.residential.project_name} - {self.amenities.title}"

class Gallery(models.Model):
    residential = models.ForeignKey(Residential, on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return f"Image #{self.pk}"

class Header(models.Model):
    residential = models.ForeignKey(Residential, on_delete=models.CASCADE, related_name="headers")    
    title = models.CharField(max_length=2000,null=True, blank=True)
    keywords = models.CharField(max_length=2000,null=True, blank=True)
    meta_description = models.CharField(max_length=5000,null=True, blank=True)
    logo = models.ImageField(null=True, blank=True,upload_to='images/')
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
    

class BankOffer(models.Model):
    residential = models.ForeignKey('Residential', on_delete=models.CASCADE, related_name="bank_offers")
    bank_approval = models.ForeignKey('utility.Bank', on_delete=models.CASCADE, related_name='booking_offers')
    title = models.CharField(max_length=200,null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

# Residential Projects End Here #

#__________________________________________________________________________________________________________


# Commercial Projects Start Here #

class CommercialProject(MPTTModel):
    CONSTRUCTION_STATUS = (
        ('Under Construction', 'Under Construction'),
        ('Ready To Move', 'Ready To Move'),
        ('New Launch', 'New Launch'),
    )
    PROPERTY_TYPE = (
        ('Commercial Office Space', 'Commercial Office Space'),
        ('Shops', 'Shops'),
        ('Showroom', 'Showroom'),
        ('Commercial Plot', 'Commercial Plot'),
        ('Co-working Space', 'Co-working Space'),
        ('Warehouse/Godown', 'Warehouse/Godown'),
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


    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    project_name = models.CharField(max_length=250)
    construction_status = models.CharField(max_length=30, choices=CONSTRUCTION_STATUS)
    property_type = models.CharField(max_length=200, choices=PROPERTY_TYPE)
    total_floors = models.CharField(max_length=10, blank=True, null=True)
    possession_year = models.CharField(max_length=200, choices=Possession_In,null=True, blank=True)

    priceing = models.CharField(max_length=50, blank=True, null=True)
    area_range = models.CharField(max_length=50, blank=True, null=True)
    featured_property = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/commercial/', blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=555, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.project_name + ' ' + self.locality.title + ' ' + self.city.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.project_name) if self.project_name else "Unnamed Commercial Project"

    class Meta:
        verbose_name_plural = "2. Commercial Projects"

    class MPTTMeta:
        order_insertion_by = ['project_name']

class CommercialBookingOffer(models.Model):
    commercial = models.ForeignKey('CommercialProject', on_delete=models.CASCADE, related_name="booking_offers")
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class CommercialWelcomeTo(models.Model):
    commercial = models.ForeignKey('CommercialProject', on_delete=models.CASCADE, related_name="welcomes")
    description = models.TextField(null=True, blank=True, max_length=5500)
    read_more = models.TextField(null=True, blank=True, max_length=5500)

    def __str__(self):
        return self.description

class CommercialLocation(models.Model):
    commercial = models.ForeignKey('CommercialProject', on_delete=models.CASCADE, related_name="locations")
    google_map_iframe = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.google_map_iframe

class CommercialWebSlider(models.Model):
    commercial = models.ForeignKey('CommercialProject', on_delete=models.CASCADE, related_name="sliders")
    image = models.ImageField(upload_to='web_slider/commercial/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.caption or f"Slider #{self.pk}"

class CommercialOverview(models.Model):
    commercial = models.ForeignKey('CommercialProject', on_delete=models.CASCADE, related_name="overviews")
    heading = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.heading

class CommercialAboutUs(models.Model):
    commercial = models.ForeignKey('CommercialProject', on_delete=models.CASCADE, related_name="aboutus")
    content = models.TextField()

    def __str__(self):
        return "About Us"

class CommercialUSP(models.Model):
    commercial = models.ForeignKey('CommercialProject', on_delete=models.CASCADE, related_name="usps")
    point = models.CharField(null=True, blank=True, max_length=150)

    def __str__(self):
        return self.point

class CommercialConfiguration(models.Model):
    commercial = models.ForeignKey('CommercialProject', on_delete=models.CASCADE, related_name="configurations")
    unit_type = models.CharField(max_length=50)  # Office, Shop, etc.
    area = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.unit_type} – {self.area}"

class CommercialConnectivity(models.Model):
    commercial = models.ForeignKey('CommercialProject', on_delete=models.CASCADE, related_name="connectivity")
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title}"

class CommercialProjectAmenities(models.Model):
    commercial = models.ForeignKey('CommercialProject', on_delete=models.CASCADE, related_name="amenities")
    amenities = models.ForeignKey(P_Amenities, on_delete=models.CASCADE, related_name="commercial_amenities")

    def __str__(self):
        return f"{self.commercial.project_name} - {self.amenities.title}"

class CommercialGallery(models.Model):
    commercial = models.ForeignKey('CommercialProject', on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to='gallery/commercial/')

    def __str__(self):
        return f"Image #{self.pk}"

class CommercialHeader(models.Model):
    commercial = models.ForeignKey('CommercialProject', on_delete=models.CASCADE, related_name="headers")
    title = models.CharField(max_length=2000, null=True, blank=True)
    keywords = models.CharField(max_length=2000, null=True, blank=True)
    meta_description = models.CharField(max_length=5000, null=True, blank=True)
    logo = models.ImageField(null=True, blank=True, upload_to='images/commercial/')
    welcome_to_bg = models.ImageField(null=True, blank=True, upload_to='headers/commercial/')
    virtual_site_visit_bg = models.ImageField(null=True, blank=True, upload_to='headers/commercial/')
    schedule_a_site_visit = models.ImageField(null=True, blank=True, upload_to='headers/commercial/')

    def __str__(self):
        return self.keywords

class CommercialRERAInfo(models.Model):
    commercial = models.ForeignKey('CommercialProject', on_delete=models.CASCADE, related_name="rera")
    qr_image = models.ImageField(null=True, blank=True, upload_to='overviewimage/commercial/')
    registration_no = models.CharField(null=True, blank=True, max_length=50)
    project_registered = models.CharField(null=True, blank=True, max_length=50)
    government_rera_authorised_advertiser = models.CharField(null=True, blank=True, max_length=150)
    site_address = models.CharField(null=True, blank=True, max_length=500)
    contact_us = models.CharField(null=True, blank=True, max_length=500)
    disclaimer = models.CharField(null=True, blank=True, max_length=1500)
    document = models.FileField(null=True, blank=True, upload_to='rera_docs/commercial/')

    def __str__(self):
        return self.registration_no

class CommercialWhyInvest(models.Model):
    commercial = models.ForeignKey('CommercialProject', on_delete=models.CASCADE, related_name="why_invest")
    title = models.CharField(max_length=350, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"Why Invest - {self.pk}"
    
    

class CommercialBankOffer(models.Model):
    commercial = models.ForeignKey('CommercialProject', on_delete=models.CASCADE, related_name="bank_offers")
    bank_approval = models.ForeignKey('utility.Bank', on_delete=models.CASCADE, related_name='commercial_booking_offers')
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

# Commercial Projects END Here #



# Projects Enquiry Start Here #


class ResidentialEnquiry(models.Model):
    residential = models.ForeignKey('Residential', on_delete=models.CASCADE, related_name='enquiries')
    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    contacted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Enquiry for {self.residential.project_name} by {self.name}"
    
    class Meta:
        verbose_name_plural='3. Residential Enquiry'



class CommercialEnquiry(models.Model):
    commercial = models.ForeignKey('CommercialProject', on_delete=models.CASCADE, related_name='enquiries')
    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    contacted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Enquiry for {self.commercial.project_name} by {self.name}"
    
    class Meta:
        verbose_name_plural='4. Commercial Enquiry'

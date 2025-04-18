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


class Residential_Property_Type(MPTTModel):
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    property_type = models.CharField(max_length=50)
    keywords = models.CharField(max_length=1000)
    description = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(unique=True, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.property_type 
    
    class Meta:
        verbose_name_plural='01. Residential Property Type'

class Commercial_Property_Type(MPTTModel):
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    property_type = models.CharField(max_length=50)
    keywords = models.CharField(max_length=1000)
    description = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(unique=True, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.property_type 
    
    class Meta:
        verbose_name_plural='02. Commercial Property Type'

class Bank(models.Model):
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='03. Bank'
   

class Amenities(models.Model):
    title = models.CharField(max_length=150,blank=True)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='04. Amenities'

class Bedroom(models.Model):
    title = models.CharField(max_length=15,blank=True)    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='05. Bedroom'

class Bathroom(models.Model):
    title = models.CharField(max_length=15,blank=True)    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='06. Bathroom'

class Bolconis(models.Model):
    title = models.CharField(max_length=15,blank=True)    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='07. Bolconis'

class Other_Room(models.Model):
    title = models.CharField(max_length=15,blank=True)    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='08. Other Room'
    
class Furnishing(models.Model):
    title = models.CharField(max_length=15,blank=True)    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='09. Furnishing'
    
class Parking(models.Model):
    title = models.CharField(max_length=15,blank=True)    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='10. Parking'

class Floor(models.Model):
    title = models.CharField(max_length=15,blank=True)    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='11. Floor'

class Total_Floor(models.Model):
    title = models.CharField(max_length=15,blank=True)    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='12. Total Flooe'

class Willing_To_Rent_Out(models.Model):
    title = models.DateField(blank=True)    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='15. Willing To Rent Out'

class Age_Of_Properties(models.Model):
    title = models.CharField(max_length=15,blank=True)    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='13. Age Of Properties'

    
class Area_type(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title   

    class Meta:
        verbose_name_plural='15. Area_type'
  

# Color
class Color(models.Model):
    title=models.CharField(max_length=100)
    color_code=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='16. Colors'

    def color_bg(self):
        return mark_safe('<div style="width:30px; height:30px; background-color:%s"></div>' % (self.color_code))

    def __str__(self):
        return self.title

class City(MPTTModel):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='images/')
    featured_city = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(City, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural='17. City'
  

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    class MPTTMeta:
        order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('city_detail', kwargs={'slug': self.slug})

    def __str__(self):  # __str__ method elaborated later in
        full_path = [self.title]  # post.  use __unicode__ in place of
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])

class Locality(MPTTModel):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)  # many to one relation with Brand

    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=1000)
    description = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='images/')
    featured_locality = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + "-- " + self.city.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + "-- " + self.city.title)
        super(Locality, self).save(*args, **kwargs)

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""
        
    class Meta:
        verbose_name_plural='18. Locality'
  


    class MPTTMeta:
        order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('locality_detail', kwargs={'slug': self.slug})

    def __str__(self):  # __str__ method elaborated later in
        full_path = [self.title]  # post.  use __unicode__ in place of
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])


class Social_Site(models.Model):    
    site=models.CharField(max_length=100)
    icone_code=models.CharField(max_length=100)

    def __str__(self):
        return self.site
    
    class Meta:
        verbose_name_plural='19. Social Site'
  

class Fine_From(models.Model):
    title = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='20. Fine_From'


Bedroom = (        
        ('1RK', '1RK'),
        ('1BHK', '1BHK'),
        ('2BHK', '2BHK'),
        ('3BHK', '3BHK'),
        ('4BHK', '4BHK'),
        ('5BHK', '5BHK'),
        ('6BHK', '6BHK'),
        ('7BHK', '7BHK'),
        ('8BHK', '8BHK'),
        ('9BHK', '9BHK'),
        ('10BHK', '10BHK'),
        ('11BHK', '11BHK'),
        ('12BHK', '12BHK'),
        ('13BHK', '13BHK'),
        ('14BHK', '14BHK'),
        ('15BHK', '15BHK'),
        ('16BHK', '16BHK'),
        ('17BHK', '17BHK'),
        ('1BHK', '18BHK'),
        ('19BHK', '19BHK'),
        ('20BHK', '20BHK'),
        ('21BHK', '21BHK'),
        ('22BHK', '22BHK'),
        ('23BHK', '23BHK'),
        ('24BHK', '24BHK'),
        ('25BHK', '25BHK'),

        
    )

Bathroom = (        
        ('1 Bathroom', '1 Bathroom'),
        ('2 Bathroom', '2 Bathroom'),
        ('3 Bathroom', '3 Bathroom'),
        ('4 Bathroom', '4 Bathroom'),
        ('5 Bathroom', '5 Bathroom'),
        ('6 Bathroom', '6 Bathroom'),
        ('7 Bathroom', '7 Bathroom'),
        ('8 Bathroom', '8 Bathroom'),
        ('9 Bathroom', '9 Bathroom'),
        ('10 Bathroom', '10 Bathroom'),


    )

Bolconis = (        
        ('1 Bolconis', '1 Bolconis'),
        ('2 Bolconis', '2 Bolconis'),
        ('3 Bolconis', '3 Bolconis'),
        ('4 Bolconis', '4 Bolconis'),
        ('5 Bolconis', '5 Bolconis'),
        ('6 Bolconis', '6 Bolconis'),
        ('7 Bolconis', '7 Bolconis'),
        ('8 Bolconis', '8 Bolconis'),
        ('9 Bolconis', '9 Bolconis'),
        ('10 Bolconis', '10 Bolconis'),


    )

Other_Room = (        
        ('Home Office', 'Home Office'),
        ('Library', 'Library'),
        ('Playroom', 'Playroom'),
        ('Home Theater', 'Home Theater'),
        ('Gym Room', 'Gym Room'),
        ('Game Room', 'Game Room'),
        ('Wine Cellar', 'Wine Cellar'),
        ('Home Bar', 'Home Bar'),
        ('Music Room', 'Music Room'),
        ('Meditation Room', 'Meditation Room'),
        ('Sauna Room', 'Sauna Room'),
        ('Sunroom/Conserv', 'Sunroom/Conserv'),

    )

Furnishing = (        
        ('Semi-Furnished', 'Semi-Furnished'),
        ('Unfurnished', 'Unfurnished'),
        ('Partially Furnished', 'Partially Furnished'),

    )

Parking = (        
        ('1 Parking', '1 Parking'),
        ('2 Parking', '2 Parking'),
        ('3 Parking', '3 Parking'),
        ('4 Parking', '4 Parking'),
        ('5 Parking', '5 Parking'),
        ('6 Parking', '6 Parking'),
        ('7 Parking', '7 Parking'),
        ('8 Parking', '8 Parking'),
        ('9 Parking', '9 Parking'),
        ('10 Parking', '10 Parking'),
        ('11 Parking', '11 Parking'),
        ('12 Parking', '12 Parking'),
        ('13 Parking', '13 Parking'),
        ('14 Parking', '14 Parking'),
        ('15 Parking', '15 Parking'),
    )


Floor_No = (        
        ('1 Floor_No', '1 Floor_No'),
        ('2 Floor_No', '2 Floor_No'),
        ('3 Floor_No', '3 Floor_No'),
        ('4 Floor_No', '4 Floor_No'),
        ('5 Floor_No', '5 Floor_No'),
        ('6 Floor_No', '6 Floor_No'),
        ('7 Floor_No', '7 Floor_No'),
        ('8 Floor_No', '8 Floor_No'),
        ('9 Floor_No', '9 Floor_No'),
        ('10 Floor_No', '10 Floor_No'),
        ('11 Floor_No', '11 Floor_No'),
        ('12 Floor_No', '12 Floor_No'),
        ('13 Floor_No', '13 Floor_No'),
        ('14 Floor_No', '14 Floor_No'),
        ('15 Floor_No', '15 Floor_No'),
        ('16 Floor_No', '16 Floor_No'),
        ('17 Floor_No', '17 Floor_No'),
        ('18 Floor_No', '18 Floor_No'),
        ('19 Floor_No', '19 Floor_No'),
        ('20 Floor_No', '20 Floor_No'),
        ('21 Floor_No', '21 Floor_No'),
        ('22 Floor_No', '22 Floor_No'),
        ('23 Floor_No', '23 Floor_No'),
        ('24 Floor_No', '24 Floor_No'),
        ('25 Floor_No', '25 Floor_No'),
        ('26 Floor_No', '26 Floor_No'),
        ('27 Floor_No', '27 Floor_No'),
        ('28 Floor_No', '28 Floor_No'),
        ('29 Floor_No', '29 Floor_No'),
        ('30 Floor_No', '30 Floor_No'),
        ('31 Floor_No', '31 Floor_No'),
        ('32 Floor_No', '32 Floor_No'),
        ('33 Floor_No', '33 Floor_No'),
        ('34 Floor_No', '34 Floor_No'),
        ('35 Floor_No', '35 Floor_No'),
        ('36 Floor_No', '36 Floor_No'),
        ('37 Floor_No', '37 Floor_No'),
        ('38 Floor_No', '38 Floor_No'),
        ('39 Floor_No', '39 Floor_No'),
        ('40 Floor_No', '40 Floor_No'),



    )

Total_Floor = (        
          ('1 Floor_No', '1 Floor_No'),
        ('2 Floor_No', '2 Floor_No'),
        ('3 Floor_No', '3 Floor_No'),
        ('4 Floor_No', '4 Floor_No'),
        ('5 Floor_No', '5 Floor_No'),
        ('6 Floor_No', '6 Floor_No'),
        ('7 Floor_No', '7 Floor_No'),
        ('8 Floor_No', '8 Floor_No'),
        ('9 Floor_No', '9 Floor_No'),
        ('10 Floor_No', '10 Floor_No'),
        ('11 Floor_No', '11 Floor_No'),
        ('12 Floor_No', '12 Floor_No'),
        ('13 Floor_No', '13 Floor_No'),
        ('14 Floor_No', '14 Floor_No'),
        ('15 Floor_No', '15 Floor_No'),
        ('16 Floor_No', '16 Floor_No'),
        ('17 Floor_No', '17 Floor_No'),
        ('18 Floor_No', '18 Floor_No'),
        ('19 Floor_No', '19 Floor_No'),
        ('20 Floor_No', '20 Floor_No'),
        ('21 Floor_No', '21 Floor_No'),
        ('22 Floor_No', '22 Floor_No'),
        ('23 Floor_No', '23 Floor_No'),
        ('24 Floor_No', '24 Floor_No'),
        ('25 Floor_No', '25 Floor_No'),
        ('26 Floor_No', '26 Floor_No'),
        ('27 Floor_No', '27 Floor_No'),
        ('28 Floor_No', '28 Floor_No'),
        ('29 Floor_No', '29 Floor_No'),
        ('30 Floor_No', '30 Floor_No'),
        ('31 Floor_No', '31 Floor_No'),
        ('32 Floor_No', '32 Floor_No'),
        ('33 Floor_No', '33 Floor_No'),
        ('34 Floor_No', '34 Floor_No'),
        ('35 Floor_No', '35 Floor_No'),
        ('36 Floor_No', '36 Floor_No'),
        ('37 Floor_No', '37 Floor_No'),
        ('38 Floor_No', '38 Floor_No'),
        ('39 Floor_No', '39 Floor_No'),
        ('40 Floor_No', '40 Floor_No'),
    )


Willing_To_Rent_Out = (        
        ('', ''),
        ('', ''),
        ('', ''),
        ('', ''),
        ('', ''),
        ('', ''),
        ('', ''),
        ('', ''),
        ('', ''),
        ('', ''),
        ('', ''),
        ('', ''),
        ('', ''),
        ('', ''),
        ('', ''),
        ('', ''),
        ('', ''),
        ('', ''),
        ('', ''),
        ('', ''),
        ('', ''),
    )


Age_Of_Properties = (        
        ('0 To 5 Years', '0 To 5 Years'),
        ('5 TO 10 Years', '5 TO 10 Years'),
        ('10 To 15 Years', '10 To 15 Years'),
        ('15 To 20 Years', '15 To 20 Years'),
        ('20 To 25 Years', '20 To 25 Years'),

    )


Area_type = (
        ('Square Feet', 'Square Feet'),
        ('Square Meter', 'Square Meter'),
        ('Square Yard', 'Square Yard'),
        ('Acre', 'Acre'),
        ('Hectare', 'Hectare'),
        ('Bigha', 'Bigha'),
        ('Biswa', 'Biswa'),

    )
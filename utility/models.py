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

class Possession_In(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title   
    
    class Meta:
        verbose_name_plural='14. Possession In'
 
    
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

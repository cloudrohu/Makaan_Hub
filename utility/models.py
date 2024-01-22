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


class Property_Type(MPTTModel):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    property_type = models.CharField(max_length=50)
    keywords = models.CharField(max_length=1000)
    description = models.TextField(max_length=5000)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(unique=True, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.property_type 



class Bank(models.Model):
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    def __str__(self):
        return self.title

class Amenities(models.Model):
    title = models.CharField(max_length=150,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    
    def __str__(self):
        return self.title

class Bedroom(models.Model):
    title = models.CharField(max_length=15,blank=True)    
    def __str__(self):
        return self.title

class Bathroom(models.Model):
    title = models.CharField(max_length=15,blank=True)    
    def __str__(self):
        return self.title

class Bolconis(models.Model):
    title = models.CharField(max_length=15,blank=True)    
    def __str__(self):
        return self.title

class Other_Room(models.Model):
    title = models.CharField(max_length=15,blank=True)    
    def __str__(self):
        return self.title
    
class Furnishing(models.Model):
    title = models.CharField(max_length=15,blank=True)    
    def __str__(self):
        return self.title
    
class Parking(models.Model):
    title = models.CharField(max_length=15,blank=True)    
    def __str__(self):
        return self.title

class Floor(models.Model):
    title = models.CharField(max_length=15,blank=True)    
    def __str__(self):
        return self.title

class Total_Floor(models.Model):
    title = models.CharField(max_length=15,blank=True)    
    def __str__(self):
        return self.title

class Willing_To_Rent_Out(models.Model):
    title = models.DateField(blank=True)    
    def __str__(self):
        return self.title

class Age_Of_Properties(models.Model):
    title = models.CharField(max_length=15,blank=True)    
    def __str__(self):
        return self.title


class Possession_In(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title    
    
class Area_type(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title    

# Color
class Color(models.Model):
    title=models.CharField(max_length=100)
    color_code=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='4. Colors'

    def color_bg(self):
        return mark_safe('<div style="width:30px; height:30px; background-color:%s"></div>' % (self.color_code))

    def __str__(self):
        return self.title


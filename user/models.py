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
# Create your models here.
from utility.models import City,Locality,Social_Site


class Developer(models.Model):
    title = models.CharField(max_length=50, unique=True)
    contact_person = models.CharField(max_length=255, null=True, blank=True)
    contact_no = models.CharField(max_length=255, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True,
                             blank=True)  # many to one relation with Brand
    email = models.EmailField(null=True, blank=True)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, null=True,
                                 blank=True)  # many to one relation with Brand
    address = models.CharField(max_length=500, null=True, blank=True)
    keywords = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=5000, null=True, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    featured_builder = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='1. Developer'


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Developer, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('developer_detail', kwargs={'slug': self.slug})

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

class Agency(models.Model):
    title = models.CharField(max_length=50, unique=True)
    contact_person = models.CharField(max_length=255, null=True, blank=True)
    contact_no = models.CharField(max_length=255, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True,
                             blank=True)  # many to one relation with Brand
    email = models.EmailField(null=True, blank=True)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, null=True,
                                 blank=True)  # many to one relation with Brand
    address = models.CharField(max_length=500, null=True, blank=True)
    keywords = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=5000, null=True, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    featured_builder = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='4. Agency'


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Agency, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('agency_detail', kwargs={'slug': self.slug})

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

class Developer_link(models.Model):
    social_site = models.ForeignKey(Social_Site, on_delete=models.CASCADE)
    Developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    link=models.CharField(max_length=100)
    
    def __str__(self):
        return self.link
    
    
    class Meta:
        verbose_name_plural='2. Developer Link'


class Agency_link(models.Model):
    social_site = models.ForeignKey(Social_Site, on_delete=models.CASCADE)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE) # many to one relation with Brand
    link=models.CharField(max_length=100)
    
    def __str__(self):
        return self.link
    
        
    class Meta:
        verbose_name_plural='5. Agency Link'


class Developer_Error(models.Model):
    agency = models.ForeignKey(Developer, on_delete=models.CASCADE) # many to one relation with Brand
    comment=models.CharField(max_length=1000)
    link=models.CharField(max_length=1000)
    
    def __str__(self):
        return self.link
    
        
    class Meta:
        verbose_name_plural='3. Developer Error'


class Agency_Error(models.Model):
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE) # many to one relation with Brand
    comment=models.CharField(max_length=1000)
    link=models.CharField(max_length=1000)
    
    def __str__(self):
        return self.link

        
    class Meta:
        verbose_name_plural='6. Agency Error'
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
from utility.models import City,Locality,Amenities
from multiselectfield import MultiSelectField

from user.models import Developer

# Create your models here.


class Sell(MPTTModel):    
    Property_Type = (
        ('Ready to move offices', 'Ready to move offices'),
        ('Shops & Retail', 'Shops & Retail'),
        ('Agricultural/Farm Land', 'Agricultural/Farm Land'),
        ('Industrial Land/Plots', 'Industrial Land/Plots'),
        ('Warehouse', 'Warehouse'),
        ('Factory & Manufacturing', 'Factory & Manufacturing'),
        ('Bare shell offices', 'Bare shell offices'),
        ('Commercial/Inst. Land', 'Commercial/Inst. Land'),
        ('Cold Storage', 'Cold Storage'),
        ('Hotel/Resorts', 'Hotel/Resorts'),
    )
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    STATUS = ( ('True', 'True'),('False', 'False'),)    
    property_type = models.CharField(max_length=55, choices=Property_Type)

    city = models.ForeignKey(City, on_delete=models.CASCADE)  # many to one relation with Brand
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE)  # many to one relation with Brand
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    min_price = models.CharField(default=0, null=True, blank=True,max_length=50, )
    max_price = models.CharField(default=0, null=True, blank=True,max_length=10, )
    min_area = models.CharField(null=True, blank=True, max_length=50)
    max_area = models.CharField(null=True, blank=True, max_length=50)
    description = models.TextField(max_length=15000,null=True, blank=True)
    amenities = MultiSelectField(choices=Amenities, max_choices=50, max_length=50,null=True, blank=True)

    project_size = models.CharField(max_length=255,null=True, blank=True)
    possession = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='images/')
    featured_property = models.BooleanField(default=False)
    status = models.CharField(max_length=55, choices=STATUS,null=True, blank=True)

    slug = models.SlugField(unique=True, null=True, blank=True,max_length=555,)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='1. Sell Property'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + ' ' + self.locality.title + ' ' + self.city.title)
        super(Sell, self).save(*args, **kwargs)

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""


class Sell_Images(models.Model):
    project=models.ForeignKey(Sell,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='5. Residential Project Images'

class Sell_Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    project=models.ForeignKey(Sell,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.CharField(max_length=250,blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status=models.CharField(max_length=10,choices=STATUS, default='New')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural='3. Residential Comment'

    def __str__(self):
        return self.subject

class CommentForm(ModelForm):
    class Meta:
        model = Sell_Comment
        fields = ['subject', 'comment', 'rate']

#___________________________________________________________________________________________________________


class Lease(MPTTModel):    
    Property_Type = (
        ('Ready to move offices', 'Ready to move offices'),
        ('Shops & Retail', 'Shops & Retail'),
        ('Agricultural/Farm Land', 'Agricultural/Farm Land'),
        ('Industrial Land/Plots', 'Industrial Land/Plots'),
        ('Warehouse', 'Warehouse'),
        ('Factory & Manufacturing', 'Factory & Manufacturing'),
        ('Bare shell offices', 'Bare shell offices'),
        ('Commercial/Inst. Land', 'Commercial/Inst. Land'),
        ('Cold Storage', 'Cold Storage'),
        ('Hotel/Resorts', 'Hotel/Resorts'),
    )
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    STATUS = ( ('True', 'True'),('False', 'False'),)    
    property_type = models.CharField(max_length=55, choices=Property_Type)

    city = models.ForeignKey(City, on_delete=models.CASCADE)  # many to one relation with Brand
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE)  # many to one relation with Brand
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    min_price = models.CharField(default=0, null=True, blank=True,max_length=50, )
    max_price = models.CharField(default=0, null=True, blank=True,max_length=10, )
    min_area = models.CharField(null=True, blank=True, max_length=50)
    max_area = models.CharField(null=True, blank=True, max_length=50)
    description = models.TextField(max_length=15000,null=True, blank=True)
    amenities = MultiSelectField(choices=Amenities, max_choices=50, max_length=50,null=True, blank=True)

    project_size = models.CharField(max_length=255,null=True, blank=True)
    possession = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='images/')
    featured_property = models.BooleanField(default=False)
    status = models.CharField(max_length=55, choices=STATUS,null=True, blank=True)

    slug = models.SlugField(unique=True, null=True, blank=True,max_length=555,)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='1. Lease Property'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + ' ' + self.locality.title + ' ' + self.city.title)
        super(Lease, self).save(*args, **kwargs)

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""


class Lease_Images(models.Model):
    project=models.ForeignKey(Lease,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='5. Residential Project Images'

class Lease_Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    project=models.ForeignKey(Lease,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.CharField(max_length=250,blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status=models.CharField(max_length=10,choices=STATUS, default='New')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural='3. Residential Comment'

    def __str__(self):
        return self.subject

class CommentForm(ModelForm):
    class Meta:
        model = Lease_Comment
        fields = ['subject', 'comment', 'rate']

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
from utility.models import City,Locality,Possession_In,Residential_Property_Type,Amenities,Bank,Bedroom,Area_type,Bathroom,Bolconis

from user.models import Developer

# Create your models here.


class Project(MPTTModel):    
    Construction_Status = (
        ('Under Construction', 'Under Construction'),
        ('New Launch', 'New Launch'),
        ('Partially Ready To Move', 'Partially Ready To Move'),
        ('Ready To Move', 'Ready To Move'),
        ('Deleverd', 'Deleverd'),
    )
    STATUS = ( ('True', 'True'),('False', 'False'),)
    
    Occupancy_Certificate = (('Yes', 'Yes'),('No', 'No'), )
    Commencement_Certificate = (('Yes', 'Yes'),('No', 'No'),)


    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)  # many to one relation with Brand
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE)  # many to one relation with Brand
    propert_type = models.ForeignKey(Residential_Property_Type, on_delete=models.CASCADE) # many to one relation with Brand
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)  # many to one relation with Brand
    possession = models.ForeignKey(Possession_In, on_delete=models.CASCADE)  # many to one relation with Brand
    min_price = models.IntegerField(default=0, null=True, blank=True, )
    max_price = models.IntegerField(default=0, null=True, blank=True, )
    min_area = models.CharField(null=True, blank=True, max_length=50)
    max_area = models.CharField(null=True, blank=True, max_length=50)
    description = models.TextField(max_length=5000,null=True, blank=True)
    Occupancy_Certificate = models.CharField(max_length=25, choices=Occupancy_Certificate,null=True, blank=True)
    Commencement_Certificate = models.CharField(max_length=25, choices=Commencement_Certificate,null=True, blank=True)
    status = models.CharField(max_length=25, choices=STATUS,null=True, blank=True)
    amenities = models.ManyToManyField(Amenities,blank=True)
    home_lone = models.ManyToManyField(Bank,blank=True)
    project_size = models.CharField(max_length=255,null=True, blank=True)
    lanch_date = models.DateField(null=True, blank=True)
    totle_unit = models.CharField(max_length=2)
    total_tower = models.CharField(max_length=2)
    construction_status = models.CharField(max_length=25, choices=Construction_Status)
    image = models.ImageField(blank=True, upload_to='images/')
    slider = models.BooleanField(default=False)
    featured_project = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='1. Project'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + ' ' + self.locality.title + ' ' + self.city.title)
        super(Project, self).save(*args, **kwargs)

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

class Images(models.Model):
    Residential_Project=models.ForeignKey(Project,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

class Floor_Plans(models.Model):
    Project=models.ForeignKey(Project,on_delete=models.CASCADE)
    bed_room=models.ForeignKey(Bedroom,on_delete=models.CASCADE, null=True, blank=True)    
    carpet_area = models.CharField(max_length=50,blank=True, null=True)
    arey_type=models.ForeignKey(Area_type,on_delete=models.CASCADE, null=True, blank=True)
    bath_room=models.ForeignKey(Bathroom,on_delete=models.CASCADE, null=True, blank=True)
    bolconis=models.ForeignKey(Bolconis,on_delete=models.CASCADE, null=True, blank=True)
    price=models.PositiveIntegerField(default=0, null=True, blank=True)
    floor_plan = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.bed_room

class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.CharField(max_length=250,blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status=models.CharField(max_length=10,choices=STATUS, default='New')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']

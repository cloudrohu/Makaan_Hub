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
from utility.models import City,Locality,Fine_From,User_Status,Visit_Type,Visit_Status,Response_Status,Business_Type,Requirent_Type,Call_Status

class Agencies(models.Model):
    Type = (
        ('agents', 'agents'),
        ('Builder Developer', 'Builder Developer'),        
    )
    agencies_type = models.CharField(max_length=25, choices=Type,null=True, blank=True)
    find_from = models.ForeignKey(Fine_From, on_delete=models.CASCADE, null=True,blank=True)  # many to one relation with Brand
    agencies_name = models.CharField(max_length=150, unique=True)
    address = models.CharField(max_length=500, null=True, blank=True)    

    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, null=True,blank=True) 
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True,blank=True)  # many to one relation with Brand
    contact_person = models.CharField(max_length=255, null=True, blank=True)
    contact_no = models.CharField(max_length=255, null=True, blank=True)
     # many to one relation with Brand
    description = models.CharField(max_length=5000, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)    

    image = models.ImageField(null=True, blank=True,upload_to='images/')
    status = models.ForeignKey(User_Status, on_delete=models.CASCADE, null=True,blank=True) 
    meeting_follow_up = models.DateTimeField(blank=True, null=True,)
    
     # many to one relation with Brand


    slug = models.SlugField(unique=True, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contact_no + ' ' + self.agencies_name + ' ' + self.locality.title
    
    class Meta:
        verbose_name_plural='1. Agencies'


    def save(self, *args, **kwargs):
        self.slug = slugify(self.agencies_name + ' ' + self.city.title)
        super(Agencies, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('Agencies_detail', kwargs={'slug': self.slug})

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
class Follow_Up(models.Model):
    comment = models.CharField(max_length=500,blank=True, null=True,)
    follow_up = models.DateTimeField(blank=True, null=True,)
    locality_city= models.ForeignKey(Locality,blank=True, null=True , on_delete=models.CASCADE)
    company = models.ForeignKey(Agencies, on_delete=models.CASCADE,null=True,blank=True) #many to one relation with Brand

    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment 
    
    class Meta:
        verbose_name_plural='4. Follow_Up'
class Meeting(models.Model):
    comment = models.CharField(max_length=500,blank=True, null=True,)
    meeting = models.DateTimeField(null=True, blank=True)
    locality_city= models.ForeignKey(Locality,blank=True, null=True , on_delete=models.CASCADE)
    company = models.ForeignKey(Agencies, on_delete=models.CASCADE,null=True,blank=True) #many to one relation with Brand

    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment 
    
    class Meta:
        verbose_name_plural='3. Meeting'
class Visit(models.Model):
    description = models.CharField(max_length=500,null=True , blank=True)
    visit_type = models.ForeignKey(Visit_Type, on_delete=models.CASCADE,null=True,blank=True) #many to one relation with Brand
    company = models.ForeignKey(Agencies, on_delete=models.CASCADE,null=True,blank=True) #many to one relation with Brand
    meet_by = models.CharField(max_length=100,null=True , blank=True)
    locality_city = models.ForeignKey(Locality, on_delete=models.CASCADE,null=True,blank=True) #many to one relation with Brand
    status = models.ForeignKey(Visit_Status, on_delete=models.CASCADE, null=True,blank=True) 
    
    followup_meeting = models.DateTimeField(null=True, blank=True)
    
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)

    def __str__(self):
        return self.description

    
    class Meta:
        verbose_name_plural='2. Today Visit'

class Meta_Response(models.Model):
    name = models.CharField(max_length=50,unique=False,null=True , blank=True)
    contact_no = models.CharField(max_length=255,null=True , blank=True)
    email_id = models.EmailField(max_length=255,null=True , blank=True)
    business_name = models.CharField(max_length=255,null=True , blank=True,unique=False,)
    description = models.CharField(max_length=500,null=True , blank=True)
    meeting_follow_up = models.DateTimeField(blank=True, null=True,)
    business_type = models.ForeignKey(Business_Type,blank=True, null=True , on_delete=models.CASCADE)
    requirent_type = models.ForeignKey(Requirent_Type,blank=True, null=True , on_delete=models.CASCADE)
    response_status = models.ForeignKey(Response_Status,blank=True, null=True , on_delete=models.CASCADE)
    call_status = models.ForeignKey(Call_Status,blank=True, null=True , on_delete=models.CASCADE)
    locality_city = models.ForeignKey(Locality,blank=True, null=True , on_delete=models.CASCADE)

    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)

    def __str__(self):
        return self.name + ' ' + self.contact_no + ' ' + self.business_name
  
    class Meta:
        verbose_name_plural='5. Meta Response'

class Respone_Meeting(models.Model):
    comment = models.CharField(max_length=500,blank=True, null=True,)
    meeting = models.DateTimeField(null=True, blank=True)
    locality_city= models.ForeignKey(Locality,blank=True, null=True , on_delete=models.CASCADE)
    respone = models.ForeignKey(Meta_Response, on_delete=models.CASCADE,null=True,blank=True) #many to one relation with Brand

    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment  
    
    class Meta:
        verbose_name_plural='6. Response Meeting'

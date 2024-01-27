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
from utility.models import City,Locality

from user.models import Agency,Developer

from project.models import Residential_Project,Commercial_Project

class Responce_Type(models.Model):    
    title = models.CharField(max_length=2500,blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Residential_Project(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    project=models.ForeignKey(Residential_Project,on_delete=models.CASCADE)
    agency=models.ForeignKey(Agency,on_delete=models.CASCADE)
    comment = models.CharField(max_length=250,blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural='1. Residential Project'

    def __str__(self):
        return self.project

class Commercial_Project(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    project=models.ForeignKey(Commercial_Project,on_delete=models.CASCADE)
    agency=models.ForeignKey(Agency,on_delete=models.CASCADE)
    comment = models.CharField(max_length=250,blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural='2. Commercial Project'

    def __str__(self):
        return self.project

class Agency_Visit(models.Model):
    agency=models.ForeignKey(Agency,on_delete=models.CASCADE)
    responce=models.ForeignKey(Responce_Type,on_delete=models.CASCADE)
    comment = models.CharField(max_length=250,blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural='3. Agency'

    def __str__(self):
        return self.project


class Developer_Visit(models.Model):
    developer=models.ForeignKey(Developer,on_delete=models.CASCADE)
    responce=models.ForeignKey(Responce_Type,on_delete=models.CASCADE)
    comment = models.CharField(max_length=250,blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural='4. Developer'

    def __str__(self):
        return self.project

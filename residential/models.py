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
from utility.models import City,Locality,Amenities,Area_type,Age_Of_Properties,Bedroom,Bathroom,Bolconis,Other_Room,Furnishing,Parking,Ownership,Floor_No,Total_Floor
from multiselectfield import MultiSelectField

from user.models import Developer

# Create your models here.


class ReSell(MPTTModel):    
    Property_Type = (
        ('1 RK Studio Apartment', '1 RK Studio Apartment'),
        ('Flat/Apartment', 'Flat/Apartment'),
        ('Independent Builder Floor', 'Independent Builder Floor'),
        ('Independent House Villa', 'Independent House Villa'),
        ('Villa/Bungalows ', 'Villa/Bungalows '),
        ('Agricultural Farm Land', 'Agricultural Farm Land'),
        ('Farm House', 'Farm House'),
    )
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    STATUS = ( ('True', 'True'),('False', 'False'),)   

    keywords = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)

    property_type = models.CharField(max_length=55, choices=Property_Type)    
    title = models.CharField(max_length=150)
    age_of_properties = models.CharField(max_length=55, choices=Age_Of_Properties,null=True, blank=True)
    possession = models.DateField(null=True, blank=True)

    
    price = models.CharField(default=0, null=True, blank=True,max_length=50, )
    area = models.CharField(null=True, blank=True, max_length=50)
    area_type = models.CharField(max_length=55, choices=Area_type,null=True, blank=True)
    bedroom = models.CharField(max_length=55, choices=Bedroom,null=True, blank=True)
    bathroom = models.CharField(max_length=55, choices=Bathroom,null=True, blank=True)
    bolconis = models.CharField(max_length=55, choices=Bolconis,null=True, blank=True)
    furnishing = models.CharField(max_length=55, choices=Furnishing,null=True, blank=True)
    parking = models.CharField(max_length=55, choices=Parking,null=True, blank=True)
    Ownership = models.CharField(max_length=55, choices=Ownership,null=True, blank=True)
    total_floor = models.CharField(max_length=55, choices=Total_Floor,null=True, blank=True)
    floor_No = models.CharField(max_length=55, choices=Floor_No,null=True, blank=True)



    description = models.TextField(max_length=15000,null=True, blank=True)
    amenities = MultiSelectField(choices=Amenities, max_choices=50, max_length=50,null=True, blank=True)
    other_room = MultiSelectField(choices=Other_Room, max_choices=50, max_length=50,null=True, blank=True)

    project_size = models.CharField(max_length=255,null=True, blank=True)
    image = models.ImageField(upload_to='images/')
    featured_property = models.BooleanField(default=False)
    youtube_link = models.CharField(max_length=250,null=True, blank=True)

    house_flat_no = models.CharField(max_length=50,null=True, blank=True)
    building_name = models.CharField(max_length=150,null=True, blank=True)
    street = models.CharField(max_length=150,null=True, blank=True)
    landmark = models.CharField(max_length=150,null=True, blank=True)
    pin_code = models.CharField(max_length=150,null=True, blank=True)

    city = models.ForeignKey(City, on_delete=models.CASCADE)  # many to one relation with Brand
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE)  # many to one relation with Brand


    status = models.CharField(max_length=55, choices=STATUS,null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True,max_length=555,)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='1. ReSell Property'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + ' ' + self.locality.title + ' ' + self.city.title)
        super(ReSell, self).save(*args, **kwargs)

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""


class ReSell_Images(models.Model):
    project=models.ForeignKey(ReSell,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='3. Sell Images'

class ReSell_Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    project=models.ForeignKey(ReSell,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.CharField(max_length=250,blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status=models.CharField(max_length=10,choices=STATUS, default='New')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural='2. ReSell Comment'

    def __str__(self):
        return self.subject

class CommentForm(ModelForm):
    class Meta:
        model = ReSell_Comment
        fields = ['subject', 'comment', 'rate']



class ReSell_Floor_Plans(models.Model):
    Project=models.ForeignKey(ReSell,on_delete=models.CASCADE)
    bed_room = models.CharField(max_length=25,choices=Bedroom,null=True, blank=True) # many to one relation with Brand
    carpet_area = models.CharField(max_length=50,blank=True, null=True)
    arey_type=models.CharField(max_length=25,choices=Area_type, null=True, blank=True)
    bath_room=models.CharField(max_length=25,choices=Bathroom, null=True, blank=True)
    bolconis=models.CharField(max_length=25,choices=Bolconis, null=True, blank=True)
    price=models.CharField(max_length=25, null=True, blank=True)
    floor_plan = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.bed_room
    
    class Meta:
        verbose_name_plural='5. Residential Project Flor Plan'

#___________________________________________________________________________________________________________

class Furnished_Amenities(models.Model):
    Project=models.ForeignKey(ReSell,on_delete=models.CASCADE)
    Wardrobe=models.CharField(max_length=25, null=True, blank=True)
    Fan=models.CharField(max_length=25, null=True, blank=True)
    Exhaust_Fan=models.CharField(max_length=25, null=True, blank=True)
    Geyser=models.CharField(max_length=25, null=True, blank=True)
    Modular_Kitchen =models.CharField(max_length=25, null=True, blank=True)
    Light=models.CharField(max_length=25, null=True, blank=True)

    AC=models.CharField(max_length=25, null=True, blank=True)
    Curtains=models.CharField(max_length=25, null=True, blank=True)
    Bed=models.CharField(max_length=25, null=True, blank=True)
    Chimney=models.CharField(max_length=25, null=True, blank=True)
    Dining_Table=models.CharField(max_length=25, null=True, blank=True)
    Microwave=models.CharField(max_length=25, null=True, blank=True)
    Fridge=models.CharField(max_length=25, null=True, blank=True)
    Sofa=models.CharField(max_length=25, null=True, blank=True)
    Stove=models.CharField(max_length=25, null=True, blank=True)
    TV=models.CharField(max_length=25, null=True, blank=True)
    Washing_Machine=models.CharField(max_length=25, null=True, blank=True)
    Water_Purifier=models.CharField(max_length=25, null=True, blank=True)


    def __str__(self):
        return self.Wardrobe
    
    class Meta:
        verbose_name_plural='6. Furnished_Amenities'

#___________________________________________________________________________________________________________

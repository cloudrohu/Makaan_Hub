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


class Bank(models.Model):
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='03. Bank'

class Willing_To_Rent_Out(models.Model):
    title = models.DateField(blank=True)    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='15. Willing To Rent Out'

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
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    featured_locality = models.BooleanField(default=False)
    keywords = models.CharField(max_length=1000)
    description = models.TextField(max_length=5000)
    slug = models.SlugField(unique=True, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + "-- " + self.city.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + "-- " + self.city.title)
        super(Locality, self).save(*args, **kwargs)
 
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


class P_Amenities(models.Model):
    title = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='amenities/', blank=True, null=True)

    def __str__(self):
        return self.title


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


class User_Status(models.Model):
    title = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.title


class Visit_Status(models.Model):
    title = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.title


class Visit_Type(models.Model):
    title = models.CharField(max_length=500,blank=True, null=True,)

    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name_plural='4. Visit_Type'


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
        ('1 ', '1'),
             ('2 ', '2'),
            ('3 ', '3'),
            ('4 ', '4'),
            ('5 ', '5'),
            ('6 ', '6'),
            ('7 ', '7'),
            ('8 ', '8'),
            ('9 ', '9'),
            ('10', '10'),
            ('11', '11'),
            ('12', '12'),
            ('13', '13'),
            ('14', '14'),
            ('15', '15'),
            ('16', '16'),
            ('17', '17'),
            ('18', '18'),
            ('19', '19'),
            ('20', '20'),
            ('21', '21'),
            ('22', '22'),
            ('23', '23'),
            ('24', '24'),
            ('25', '25'),
            ('26', '26'),
            ('27', '27'),
            ('28', '28'),
            ('29', '29'),
            ('30', '30'),
            ('31', '31'),
            ('32', '32'),
            ('33', '33'),
            ('34', '34'),
            ('35', '35'),
            ('36', '36'),
            ('37', '37'),
            ('38', '38'),
            ('39', '39'),
            ('40', '40'),
            ('41', '41'),
            ('42', '42'),
            ('43', '43'),
            ('44', '44'),
            ('45', '45'),
            ('46', '46'),
            ('47', '47'),
            ('48', '48'),
            ('49', '49'),
            ('50', '50'),
    )

Total_Floor = (        
            ('1 ', '1'),
             ('2 ', '2'),
            ('3 ', '3'),
            ('4 ', '4'),
            ('5 ', '5'),
            ('6 ', '6'),
            ('7 ', '7'),
            ('8 ', '8'),
            ('9 ', '9'),
            ('10', '10'),
            ('11', '11'),
            ('12', '12'),
            ('13', '13'),
            ('14', '14'),
            ('15', '15'),
            ('16', '16'),
            ('17', '17'),
            ('18', '18'),
            ('19', '19'),
            ('20', '20'),
            ('21', '21'),
            ('22', '22'),
            ('23', '23'),
            ('24', '24'),
            ('25', '25'),
            ('26', '26'),
            ('27', '27'),
            ('28', '28'),
            ('29', '29'),
            ('30', '30'),
            ('31', '31'),
            ('32', '32'),
            ('33', '33'),
            ('34', '34'),
            ('35', '35'),
            ('36', '36'),
            ('37', '37'),
            ('38', '38'),
            ('39', '39'),
            ('40', '40'),
            ('41', '41'),
            ('42', '42'),
            ('43', '43'),
            ('44', '44'),
            ('45', '45'),
            ('46', '46'),
            ('47', '47'),
            ('48', '48'),
            ('49', '49'),
            ('50', '50'),       
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
        (' under construction', ' under construction'),
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

Amenities = (
        ('Air Condition', 'Air Condition'),
        ('Badminton Court', 'Badminton Court'),
        ('balcony', 'balcony'),
        ('Barbeque', 'Barbeque'),
        ('Basket Ball', 'Basket Ball'),
        ('Car Parking', 'Car Parking'),
        ('CCTV', 'CCTV'),
        ('club house', 'club house'),
        ('Community hall', 'Community hall'),
        ('Conference room', 'Conference room'),
        ('Creche Area', 'Creche Area'),
        ('Cricket Pitch', 'Cricket Pitch'),
        ('Curtains', 'Curtains'),
        ('Dining Table', 'Dining Table'),
        ('Electric Vehicle Charging Socket', 'Electric Vehicle Charging Socket'),
        ('Electrical Switchboard', 'Electrical Switchboard'),
        ('Elevator', 'Elevator'),
        ('Exhaust Fan', 'Exhaust Fan'),
        ('Fans', 'Fans'),
        ('Fire Fighting Equipment', 'Fire Fighting Equipment'),
        ('Garden', 'Garden'),
        ('Geysers', 'Geysers'),
        ('Grand lobby', 'Grand lobby'),
        ('Gymnasium', 'Gymnasium'),
        ('Hammock', 'Hammock'),
        ('Indoor Games', 'Indoor Games'),
        ('Intercom', 'Intercom'),
        ('jacuzzi', 'jacuzzi'),
        ('Jogging track', 'Jogging track'),
        ('Kids Play Area', 'Kids Play Area'),
        ('Library', 'Library'),
        ('Lights', 'Lights'),
        ('Live chess', 'Live chess'),
        ('Microwave', 'Microwave'),
        ('mini theater', 'mini theater'),
        ('Modular Kitchen', 'Modular Kitchen'),
        ('Multipurpose Hall', 'Multipurpose Hall'),
        ('Rain Water Harvesting', 'Rain Water Harvesting'),
        ('Reflexology Path', 'Reflexology Path'),
        ('Refrigerator', 'Refrigerator'),
        ('Regular Water Supply', 'Regular Water Supply'),
        ('Rooftop garden', 'Rooftop garden'),
        ('sauna bath', 'sauna bath'),
        ('Security', 'Security'),
        ('Senior citizen area', 'Senior citizen area'),
        ('Society Office', 'Society Office'),
        ('Sofa', 'Sofa'),
        ('Solar Power', 'Solar Power'),
        ('Spa', 'Spa'),
        ('Squash court', 'Squash court'),
        ('Stainless Steel Sink', 'Stainless Steel Sink'),
        ('Stove', 'Stove'),
        ('Swimming Pool', 'Swimming Pool'),
        ('Terrace', 'Terrace'),
        ('Video Door phone', 'Video Door phone'),
        ('Volleyball Court', 'Volleyball Court'),
        ('Wardrobe T.V', 'Wardrobe T.V'),
        ('Washing Machine', 'Washing Machine'),
        ('Water Purifier', 'Water Purifier'),
        ('Water Softener', 'Water Softener'),
        ('Wi fi', 'Wi fi'),
        ('yoga deck', 'yoga deck'),
             
        
    )

Ownership = (
        ('Free Hold', 'Free Hold'),
        ('Lease Hold', 'Lease Hold'),
        ('Co-Operative Society', 'Co-Operative Society'),
        ('Power of Attorney', 'Power of Attorney'),      

    )

Furnishing = (
        ('Fully Furnished', 'Fully Furnished'),
        ('Semi Furnished', 'Semi Furnished'),
        ('Unfurnished', 'Unfurnished'),
        ('Ready To Furnished', 'Ready To Furnished'),
        ('Partially Furnished', 'Partially Furnished'),


    )


class Response_Status(models.Model):
    name = models.CharField(max_length=100,unique=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name_plural='5. Response Status'


class Business_Type(models.Model):
    name = models.CharField(max_length=100,unique=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name_plural='5. Business Type'


class Requirent_Type(models.Model):
    name = models.CharField(max_length=100,unique=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name_plural='5. Requirent Type'


class Call_Status(models.Model):
    name = models.CharField(max_length=100,unique=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name_plural='5. Call Status'
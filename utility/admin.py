from django.contrib import admin
from . models import *
# Register your models here.
class ColorAdmin(admin.ModelAdmin):
    list_display = ['id','title','color_code',]
    list_per_page = 30 



admin.site.register(Bank,)
admin.site.register(Amenities,)
admin.site.register(Bedroom,)
admin.site.register(Bathroom,)
admin.site.register(Bolconis,)
admin.site.register(Other_Room,)
admin.site.register(Furnishing,)
admin.site.register(Parking,)
admin.site.register(Floor,)
admin.site.register(Total_Floor,)
admin.site.register(Willing_To_Rent_Out,)
admin.site.register(Age_Of_Properties,)
admin.site.register(Property_Type,)
admin.site.register(Color,ColorAdmin)


import admin_thumbnails
from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin
from . models import *
# Register your models here.
class ReSell_ImagesInline(admin.TabularInline):
    list_display = ['id']
    model = ReSell_Images   
    extra = 1


class ReSell_Floor_PlansInline(admin.TabularInline):
    list_display = ['id']
    model = ReSell_Floor_Plans   
    extra = 1


class Furnished_AmenitiesInline(admin.TabularInline):
    list_display = ['id']
    model = Furnished_Amenities   
    extra = 1


@admin_thumbnails.thumbnail('image')
class ReSellAdmin(admin.ModelAdmin):
    list_display = ['id','image_thumbnail','title','locality','city','property_type','price','area']
    list_filter = ['locality','city','property_type',]
    search_fields = ['title',]
    inlines = [ReSell_ImagesInline,ReSell_Floor_PlansInline,Furnished_AmenitiesInline]
    list_per_page = 30 


class ReSellCommentAdmin(admin.ModelAdmin):
    list_display = ['user','subject','comment', 'project','status','create_at','rate','ip']
    list_filter = ['status']
    list_editable = ['status']
    readonly_fields = ('subject','comment','ip','user','project','rate','id')



admin.site.register(Furnished_Amenities,)
admin.site.register(ReSell_Floor_Plans,)
admin.site.register(ReSell_Images,)
admin.site.register(ReSell,ReSellAdmin)
admin.site.register(ReSell_Comment,ReSellCommentAdmin)


#___________________________________________________________________________________________________________

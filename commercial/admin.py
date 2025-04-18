import admin_thumbnails
from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin
from . models import *
# Register your models here.
class Sell_ImagesInline(admin.TabularInline):
    list_display = ['id']
    model = Sell_Images   
    extra = 1

@admin_thumbnails.thumbnail('image')
class SellAdmin(admin.ModelAdmin):
    list_display = ['id','image_thumbnail','title','locality','city','property_type','min_price','max_price']
    list_filter = ['locality','city','property_type',]
    search_fields = ['title',]
    inlines = [Sell_ImagesInline,]
    list_per_page = 30 


class SellCommentAdmin(admin.ModelAdmin):
    list_display = ['user','subject','comment', 'project','status','create_at','rate','ip']
    list_filter = ['status']
    list_editable = ['status']
    readonly_fields = ('subject','comment','ip','user','project','rate','id')



admin.site.register(Sell_Images,)
admin.site.register(Sell,SellAdmin)
admin.site.register(Sell_Comment,SellCommentAdmin)


#___________________________________________________________________________________________________________

class Lease_ImagesInline(admin.TabularInline):
    list_display = ['id']
    model = Lease_Images   
    extra = 1

@admin_thumbnails.thumbnail('image')
class LeaseAdmin(admin.ModelAdmin):
    list_display = ['id','image_thumbnail','title','locality','city','property_type','min_price','max_price']
    list_filter = ['locality','city','property_type',]
    search_fields = ['title',]
    inlines = [Lease_ImagesInline,]
    list_per_page = 30 


class LeaseCommentAdmin(admin.ModelAdmin):
    list_display = ['user','subject','comment', 'project','status','create_at','rate','ip']
    list_filter = ['status']
    list_editable = ['status']
    readonly_fields = ('subject','comment','ip','user','project','rate','id')



admin.site.register(Lease_Images,)
admin.site.register(Lease,LeaseAdmin)
admin.site.register(Lease_Comment,LeaseCommentAdmin)
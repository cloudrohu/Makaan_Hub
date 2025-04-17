import admin_thumbnails
from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin
from . models import *
# Register your models here.
class Sell_Property_ImagesInline(admin.TabularInline):
    list_display = ['id']
    model = Sell_Property_Images   
    extra = 1

@admin_thumbnails.thumbnail('image')
class Sell_PropertyAdmin(admin.ModelAdmin):
    list_display = ['id','image_thumbnail','title','locality','city','property_type','min_price','max_price']
    list_filter = ['locality','city','property_type',]
    search_fields = ['title',]
    inlines = [Sell_Property_ImagesInline,]
    list_per_page = 30 


class Sell_PropertyCommentAdmin(admin.ModelAdmin):
    list_display = ['user','subject','comment', 'project','status','create_at','rate','ip']
    list_filter = ['status']
    list_editable = ['status']
    readonly_fields = ('subject','comment','ip','user','project','rate','id')



admin.site.register(Sell_Property_Images,)
admin.site.register(Sell_Property,Sell_PropertyAdmin)
admin.site.register(Sell_Property_Comment,Sell_PropertyCommentAdmin)


#___________________________________________________________________________________________________________

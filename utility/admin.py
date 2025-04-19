import admin_thumbnails
from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin
from . models import *
# Register your models here.
class ColorAdmin(admin.ModelAdmin):
    list_display = ['id','title','color_code',]
    list_per_page = 30 

@admin_thumbnails.thumbnail('image')
class CityAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('id','tree_actions', 'indented_title', 'image_thumbnail',
                    )
    list_display_links = ('indented_title',)
    list_per_page = 30 
    search_fields = ['title'] 
    

@admin_thumbnails.thumbnail('image')
class LocalityAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('id','tree_actions','city', 'indented_title', 'image_thumbnail',
                   )
    list_display_links = ('indented_title',)
    list_per_page = 30 
    search_fields = ['title']
    list_filter = ['city']


admin.site.register(Bank,)
admin.site.register(City,CityAdmin)
admin.site.register(Locality,LocalityAdmin)
admin.site.register(Fine_From,)


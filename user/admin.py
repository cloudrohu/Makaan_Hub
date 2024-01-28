import admin_thumbnails
from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin
from . models import *
# Register your models here.

class Developer_MeetingInline(admin.TabularInline):
    list_display = ['id']
    model = Developer_Meeting  
    extra = 1


class Developer_linkInline(admin.TabularInline):
    list_display = ['id']
    model = Developer_link   
    extra = 1

class Developer_ErrorInline(admin.TabularInline):
    list_display = ['id']
    model = Developer_Error   
    extra = 1

class Agency_MeetinInline(admin.TabularInline):
    list_display = ['id']
    model = Agency_Meeting  
    extra = 1


class Agency_linkInline(admin.TabularInline):
    list_display = ['id']
    model = Agency_link   
    extra = 1

class Agency_ErrorInline(admin.TabularInline):
    list_display = ['id']
    model = Agency_Error   
    extra = 1


@admin_thumbnails.thumbnail('image')
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ['id','image_thumbnail','title','find_from', 'contact_person','contact_no','email','google_map', 'web_site', 'address','locality','city',]
    list_filter = ('locality','city','find_from',) 
    search_fields = ['title','contact_no','contact_person','web_site']
    list_per_page = 30 
    inlines = [Developer_linkInline,Developer_ErrorInline,Developer_MeetingInline]


@admin_thumbnails.thumbnail('image')
class AgencyAdmin(admin.ModelAdmin):
    list_display = ['id','image_thumbnail','title', 'find_from', 'contact_person','contact_no','email', 'google_map', 'web_site','address','locality','city',]
    list_filter = ('locality','city','find_from') 
    search_fields = ['title','contact_no','contact_person','web_site']
    list_per_page = 30 
    inlines = [Agency_linkInline,Agency_ErrorInline,Agency_MeetinInline]

class Developer_MeetingAdmin(admin.ModelAdmin):
    list_display = ['id','developer','meeting_date','comment','create_at','update_at']
    list_filter = ('meeting_date','create_at','update_at') 
    list_per_page = 30 

class Agency_MeetingAdmin(admin.ModelAdmin):
    list_display = ['id','agency','meeting_date','comment','create_at','update_at']
    list_filter = ('meeting_date','create_at','update_at') 
    list_per_page = 30 

admin.site.register(Agency,AgencyAdmin)
admin.site.register(Developer,DeveloperAdmin)
admin.site.register(Developer_link,)
admin.site.register(Developer_Error,)
admin.site.register(Agency_link,)
admin.site.register(Agency_Error,)


admin.site.register(Agency_Meeting,Agency_MeetingAdmin)
admin.site.register(Developer_Meeting,Developer_MeetingAdmin)
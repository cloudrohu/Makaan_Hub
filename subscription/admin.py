import admin_thumbnails
from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin

from .models import *



class Follow_UpInline(admin.TabularInline):
    model = Follow_Up
    extra = 1
    show_change_link = True

class MeetingInline(admin.TabularInline):
    model = Meeting
    extra = 1
    show_change_link = True

class VisitInline(admin.TabularInline):
    model = Visit
    extra = 1
    show_change_link = True


@admin_thumbnails.thumbnail('image')
class AgenciesAdmin(admin.ModelAdmin):
    list_display = ['id','status', 'image_thumbnail','agencies_type', 'agencies_name', 'contact_person', 'contact_no',  'description', 'meeting_follow_up','email','city', 'locality', 'address','create_at','update_at', 'find_from',]    
    
    list_filter = ['create_at','city', 'locality','status','meeting_follow_up']
    search_fields = ['agencies_name', 'contact_person','contact_person', 'description','email']
    list_editable = ('meeting_follow_up','city', 'locality', 'status',)
    list_per_page = 20
    inlines = [Follow_UpInline,MeetingInline,VisitInline]


class MeetingAdmin(admin.ModelAdmin):
    list_display = ['id','company', 'meeting','comment','create_at','update_at']    
    
    list_filter = ('meeting','create_at','update_at',) 
    list_per_page = 20 


class Follow_UpAdmin(admin.ModelAdmin):
    list_display = ['id', 'company', 'follow_up','comment', 'create_at','update_at']   
    
    list_filter = ('follow_up','create_at','update_at',) 
    list_per_page = 20 

class VisitAdmin(admin.ModelAdmin):
    list_display = ['id','visit_type', 'company', 'meet_by', 'description', 'followup_meeting','create_at','update_at']   
    
    list_filter = ('followup_meeting','create_at','update_at',) 
    list_per_page = 20 


admin.site.register(Follow_Up,Follow_UpAdmin)
admin.site.register(Meeting,MeetingAdmin)
admin.site.register(Visit,VisitAdmin)
admin.site.register(Agencies,AgenciesAdmin)









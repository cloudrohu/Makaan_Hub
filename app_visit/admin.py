import admin_thumbnails
from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin
from . models import *



class Residential_ProjectAdmin(admin.ModelAdmin):
    list_display = ['id','project','agency','comment','create_at','update_at']
    readonly_fields = ('create_at','update_at')
admin.site.register(Residential_Project,Residential_ProjectAdmin)


class Commercial_ProjectAdmin(admin.ModelAdmin):
    list_display = ['id','project','agency','comment','create_at','update_at']
    readonly_fields = ('create_at','update_at')
admin.site.register(Commercial_Project,Commercial_ProjectAdmin)


class Agency_VisitAdmin(admin.ModelAdmin):
    list_display = ['id','agency','comment','create_at','update_at']
    readonly_fields = ('create_at','update_at')
admin.site.register(Agency_Visit,Agency_VisitAdmin)


class Developer_VisitAdmin(admin.ModelAdmin):
    list_display = ['id','developer','comment','create_at','update_at']
    readonly_fields = ('create_at','update_at')
admin.site.register(Developer_Visit,Developer_VisitAdmin)

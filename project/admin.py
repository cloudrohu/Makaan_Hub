import admin_thumbnails
from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin
from . models import *
# Register your models here.
class Residential_Project_ImagesInline(admin.TabularInline):
    list_display = ['id']
    model = Residential_Project_Images   
    extra = 1

class Residential_Project_Floor_Plans_ImagesInline(admin.TabularInline):
    list_display = ['id']
    model = Residential_Project_Floor_Plans   
    extra = 1


@admin_thumbnails.thumbnail('image')
class Residential_ProjectAdmin(admin.ModelAdmin):
    list_display = ['id','image_thumbnail','title','locality','city','propert_type', 'developer', 'possession','featured_project','slider']
    list_filter = ['locality','city','propert_type', 'developer', 'possession',]
    search_fields = ['title']
    inlines = [Residential_Project_ImagesInline,Residential_Project_Floor_Plans_ImagesInline]
    list_per_page = 30 


class Residential_Project_CommentAdmin(admin.ModelAdmin):
    list_display = ['user','subject','comment', 'project','status','create_at','rate','ip']
    list_filter = ['status']
    list_editable = ['status']
    readonly_fields = ('subject','comment','ip','user','project','rate','id')



admin.site.register(Possession_In,)
admin.site.register(Residential_Project_Images,)
admin.site.register(Residential_Project_Floor_Plans,)
admin.site.register(Residential_Project,Residential_ProjectAdmin)
admin.site.register(Residential_Project_Comment,Residential_Project_CommentAdmin)


#___________________________________________________________________________________________________________

class Commercial_Project_project_ImagesInline(admin.TabularInline):
    list_display = ['id']
    model = Commercial_Project_Images   
    extra = 1

class Commercial_Project_Floor_Plans_ImagesInline(admin.TabularInline):
    list_display = ['id']
    model = Commercial_Project_Floor_Plans   
    extra = 1


@admin_thumbnails.thumbnail('image')
class Commercial_Project_Admin(admin.ModelAdmin):
    list_display = ['id','image_thumbnail','title','locality','city','propert_type', 'developer', 'possession','featured_project','slider']

    list_filter = ['locality','city','propert_type', 'developer', 'possession',]
    search_fields = ['title']
    inlines = [Commercial_Project_project_ImagesInline,Commercial_Project_Floor_Plans_ImagesInline]
    list_per_page = 30 


class Commercial_Project_CommentAdmin(admin.ModelAdmin):
    list_display = ['user','subject','comment', 'project','status','create_at','rate','ip']
    list_filter = ['status']
    list_editable = ['status']
    readonly_fields = ('subject','comment','ip','user','project','rate','id')



admin.site.register(Commercial_Project_Images,)
admin.site.register(Commercial_Project_Floor_Plans,)
admin.site.register(Commercial_Project,Commercial_Project_Admin)
admin.site.register(Commercial_Project_Comment,Commercial_Project_CommentAdmin)
import admin_thumbnails
from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin
from . models import *
# Register your models here.


class project_ImagesInline(admin.TabularInline):
    list_display = ['id']
    model = Images   
    extra = 1

class Floor_Plans_ImagesInline(admin.TabularInline):
    list_display = ['id']
    model = Floor_Plans   
    extra = 1


@admin_thumbnails.thumbnail('image')
class project_ImagesInline(admin.TabularInline):
    list_display = ['id']
    model = Images
   
    extra = 1


@admin_thumbnails.thumbnail('image')
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id','image_thumbnail','title','locality','city','propert_type', 'developer', 'possession','featured_project','slider']

    list_filter = ['locality','city','propert_type', 'developer', 'possession',]
    search_fields = ['title']
    inlines = [project_ImagesInline,Floor_Plans_ImagesInline]
    list_per_page = 30 


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','subject','comment', 'project','status','create_at','rate','ip']
    list_filter = ['status']
    list_editable = ['status']
    readonly_fields = ('subject','comment','ip','user','project','rate','id')



admin.site.register(Possession_In,)
admin.site.register(Images,)
admin.site.register(Floor_Plans,)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Comment,CommentAdmin)
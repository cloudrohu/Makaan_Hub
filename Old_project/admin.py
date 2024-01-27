import admin_thumbnails
from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin
from . models import *

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
class CityAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('id','tree_actions', 'indented_title', 'image_thumbnail',
                    'related_locality_count','project_count',)
    list_display_links = ('indented_title',)
    list_per_page = 30 
    search_fields = ['title']    
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
       
        # Add non cumulative product count
        qs = City.objects.add_related_count(qs,
                 Locality,
                 'city',
                 'locality_count',
                 cumulative=False)
        qs = City.objects.add_related_count(qs,
                 Project,
                 'city',
                 'project_count',
                 cumulative=False)
        return qs      
   
    def project_count(self, instance):
        return instance.project_count
    project_count.short_description = 'Related Project (for this specific Locality)'
        

    def related_locality_count(self, instance):
        return instance.locality_count
    related_locality_count.short_description = 'Related Locality (for this specific City)'

@admin_thumbnails.thumbnail('image')
class LocalityAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('id','tree_actions','city', 'indented_title', 'image_thumbnail',
                    'project_count',)
    list_display_links = ('indented_title',)
    list_per_page = 30 
    search_fields = ['title']
    list_filter = ['city']
    
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
       
        # Add non cumulative product count
        qs = Locality.objects.add_related_count(qs,
                 Project,
                 'locality',
                 'project_count',
                 cumulative=False)
        return qs

    def project_count(self, instance):
        return instance.project_count
    project_count.short_description = 'Related Project (for this specific Locality)'

@admin_thumbnails.thumbnail('image')
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ['id','image_thumbnail','title', 'contact_person','contact_no','email','address','locality','city',]
    
    list_filter = ('locality','city',) 
    search_fields = ['title']
    list_per_page = 30 


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


admin.site.register(City,CityAdmin)
admin.site.register(Locality,LocalityAdmin)
admin.site.register(Developer,DeveloperAdmin)
admin.site.register(Possession_In,)
admin.site.register(Images,)
admin.site.register(Floor_Plans,)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Comment,CommentAdmin)



from django.contrib import admin
from .models import *
import admin_thumbnails

# Register your models here.

class Social_LinkInline(admin.TabularInline):
    list_display = ['id']
    model = Social_Link   
    extra = 1
class SettingtAdmin(admin.ModelAdmin):
    list_display = ['title','company', 'update_at','status']

class Social_SiteAdmin(admin.ModelAdmin):
    list_display = ['id','title']

class Social_LinkAdmin(admin.ModelAdmin):
    list_display = ['id','our_team','social_site','link',]


@admin_thumbnails.thumbnail('image')
class Our_TeamAdmin(admin.ModelAdmin):
    list_display = ['id','title','image_thumbnail',]
    inlines = [Social_LinkInline,]

@admin_thumbnails.thumbnail('image')
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['id','name','image_thumbnail',]
    


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name','subject', 'update_at','status','note','message','email','ip',]
    list_editable = ['status','note']
    readonly_fields =('name','subject','email','message','ip')
    list_filter = ['status']

admin.site.register(Setting,SettingtAdmin)

class About_PageAdmin(admin.ModelAdmin):
    list_display = ['id','title','keywords','description',]

admin.site.register(About_Page,About_PageAdmin)

class Contact_PageAdmin(admin.ModelAdmin):
    list_display = ['id','title','keywords','description',]
admin.site.register(Contact_Page,Contact_PageAdmin)

admin.site.register(ContactMessage,ContactMessageAdmin)
admin.site.register(Social_Link,Social_LinkAdmin)
admin.site.register(Social_Site,)
admin.site.register(Our_Team,Our_TeamAdmin)
admin.site.register(Testimonial,TestimonialAdmin)


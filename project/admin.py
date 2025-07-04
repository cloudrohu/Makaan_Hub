import admin_thumbnails
from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin
from . models import *




class WelcomeToInline(admin.StackedInline):
    model = WelcomeTo
    extra = 1

class LocationInline(admin.StackedInline):
    model = Location
    extra = 1

class WebSliderInline(admin.StackedInline):
    model = WebSlider
    extra = 3

class OverviewInline(admin.StackedInline):
    model = Overview
    extra = 1

class AboutUsInline(admin.StackedInline):
    model = AboutUs
    extra = 1

class USPInline(admin.StackedInline):
    model = USP
    extra = 4

class ConfigurationInline(admin.StackedInline):
    model = Configuration
    extra = 2

class Project_AmenitiesInline(admin.StackedInline):
    model = Project_Amenities
    extra = 4

class GalleryInline(admin.StackedInline):
    model = Gallery
    extra = 3

class HeaderInline(admin.StackedInline):
    model = Header
    extra = 1

class RERA_InfoInline(admin.StackedInline):
    model = RERA_Info
    extra = 1

class ConnectivityInline(admin.StackedInline):
    model = Connectivity
    extra = 4

class WhyInvestInline(admin.StackedInline):
    model = WhyInvest
    extra = 4

class BookingOfferInline(admin.StackedInline):
    model = BookingOffer
    extra = 3

@admin_thumbnails.thumbnail('image')

class ResidentialAdmin(admin.ModelAdmin):
    inlines = [
        WelcomeToInline,
        LocationInline,
        WebSliderInline,
        OverviewInline,
        AboutUsInline,
        USPInline,
        ConfigurationInline,
        Project_AmenitiesInline,
        GalleryInline,
        HeaderInline,
        RERA_InfoInline,
        ConnectivityInline,
        WhyInvestInline,
        BookingOfferInline,
    ]
    list_display = ['id','image_thumbnail','project_name','developer', 'active','featured_property', 'locality','city','propert_type','possession_year']
    list_editable = [ 'project_name','developer','active','featured_property','locality','city','propert_type',]
    list_filter = ['developer','active','featured_property','locality','city','propert_type','possession_year']
    search_fields = ['project_name',]


admin.site.register(Residential,ResidentialAdmin)

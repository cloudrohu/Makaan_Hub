import admin_thumbnails
from django.contrib import admin
from django.utils.html import format_html


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
    list_per_page = 20


    def image_preview(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return format_html('<img src="{}" style="height:40px;"/>', obj.image.url)
        return "No Image"
    image_preview.short_description = "Image"
admin.site.register(Residential,ResidentialAdmin)




import admin_thumbnails
from django.contrib import admin
from .models import (
    CommercialProject, CommercialBookingOffer, CommercialWelcomeTo, CommercialLocation, CommercialWebSlider, CommercialOverview,
    CommercialAboutUs, CommercialUSP, CommercialConfiguration, CommercialProjectAmenities,
    CommercialGallery, CommercialHeader, CommercialRERAInfo, CommercialWhyInvest, CommercialBankOffer, CommercialConnectivity
)

class CommercialWelcomeToInline(admin.StackedInline):
    model = CommercialWelcomeTo
    extra = 1

class CommercialLocationInline(admin.StackedInline):
    model = CommercialLocation
    extra = 1

class CommercialWebSliderInline(admin.StackedInline):
    model = CommercialWebSlider
    extra = 3

class CommercialOverviewInline(admin.StackedInline):
    model = CommercialOverview
    extra = 1

class CommercialAboutUsInline(admin.StackedInline):
    model = CommercialAboutUs
    extra = 1

class CommercialUSPInline(admin.StackedInline):
    model = CommercialUSP
    extra = 4

class CommercialConfigurationInline(admin.StackedInline):
    model = CommercialConfiguration
    extra = 2

class CommercialProjectAmenitiesInline(admin.StackedInline):
    model = CommercialProjectAmenities
    extra = 4

class CommercialGalleryInline(admin.StackedInline):
    model = CommercialGallery
    extra = 3

class CommercialHeaderInline(admin.StackedInline):
    model = CommercialHeader
    extra = 1

class CommercialRERAInfoInline(admin.StackedInline):
    model = CommercialRERAInfo
    extra = 1

class CommercialConnectivityInline(admin.StackedInline):
    model = CommercialConnectivity
    extra = 4

class CommercialWhyInvestInline(admin.StackedInline):
    model = CommercialWhyInvest
    extra = 4

class CommercialBookingOfferInline(admin.StackedInline):
    model = CommercialBookingOffer
    extra = 3

class CommercialBankOfferInline(admin.StackedInline):
    model = CommercialBankOffer
    extra = 2

@admin_thumbnails.thumbnail('image')
class CommercialProjectAdmin(admin.ModelAdmin):
    inlines = [
        CommercialWelcomeToInline,
        CommercialLocationInline,
        CommercialWebSliderInline,
        CommercialOverviewInline,
        CommercialAboutUsInline,
        CommercialUSPInline,
        CommercialConfigurationInline,
        CommercialProjectAmenitiesInline,
        CommercialGalleryInline,
        CommercialHeaderInline,
        CommercialRERAInfoInline,
        CommercialConnectivityInline,
        CommercialWhyInvestInline,
        CommercialBookingOfferInline,
        CommercialBankOfferInline,
    ]
    list_display = [
        'id', 'image_thumbnail', 'project_name', 'developer', 'active', 'featured_property',
        'locality', 'city', 'property_type', 'possession_year'
    ]
    list_editable = [
        'project_name', 'developer', 'active', 'featured_property', 'locality', 'city', 'property_type',
    ]
    list_filter = [
        'developer', 'active', 'featured_property', 'locality', 'city', 'property_type', 'possession_year'
    ]
    search_fields = ['project_name', ]

admin.site.register(CommercialProject, CommercialProjectAdmin)


@admin.register(ResidentialEnquiry)
class ResidentialEnquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'residential', 'name', 'email', 'phone', 'contacted_on')
    search_fields = ('name', 'email', 'phone', 'residential__project_name')
    list_filter = ('contacted_on', 'residential')

@admin.register(CommercialEnquiry)
class CommercialEnquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'commercial', 'name', 'email', 'phone', 'contacted_on')
    search_fields = ('name', 'email', 'phone', 'commercial__project_name')
    list_filter = ('contacted_on', 'commercial')




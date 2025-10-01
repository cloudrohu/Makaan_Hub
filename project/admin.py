import admin_thumbnails
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import (
    Residential, WelcomeTo, Location, WebSlider, Overview, AboutUs, USP, Configuration,
    Project_Amenities, Gallery, Header, RERA_Info, Connectivity, WhyInvest, BookingOffer,
    CommercialProject, CommercialBookingOffer, CommercialWelcomeTo, CommercialLocation, 
    CommercialWebSlider, CommercialOverview, CommercialAboutUs, CommercialUSP, 
    CommercialConfiguration, CommercialProjectAmenities, CommercialGallery, CommercialHeader, 
    CommercialRERAInfo, CommercialWhyInvest, CommercialBankOffer, CommercialConnectivity,
    ResidentialEnquiry, CommercialEnquiry
)

# ----------------------------------------------------------------
# RESOURCES
# ----------------------------------------------------------------
class ResidentialResource(resources.ModelResource):
    class Meta:
        model = Residential

class CommercialProjectResource(resources.ModelResource):
    class Meta:
        model = CommercialProject

class ResidentialEnquiryResource(resources.ModelResource):
    class Meta:
        model = ResidentialEnquiry

class CommercialEnquiryResource(resources.ModelResource):
    class Meta:
        model = CommercialEnquiry


# Inline models resources (Residential)
class WelcomeToResource(resources.ModelResource):
    class Meta: model = WelcomeTo

class LocationResource(resources.ModelResource):
    class Meta: model = Location

class WebSliderResource(resources.ModelResource):
    class Meta: model = WebSlider

class OverviewResource(resources.ModelResource):
    class Meta: model = Overview

class AboutUsResource(resources.ModelResource):
    class Meta: model = AboutUs

class USPResource(resources.ModelResource):
    class Meta: model = USP

class ConfigurationResource(resources.ModelResource):
    class Meta: model = Configuration

class ProjectAmenitiesResource(resources.ModelResource):
    class Meta: model = Project_Amenities

class GalleryResource(resources.ModelResource):
    class Meta: model = Gallery

class HeaderResource(resources.ModelResource):
    class Meta: model = Header

class RERAInfoResource(resources.ModelResource):
    class Meta: model = RERA_Info

class ConnectivityResource(resources.ModelResource):
    class Meta: model = Connectivity

class WhyInvestResource(resources.ModelResource):
    class Meta: model = WhyInvest

class BookingOfferResource(resources.ModelResource):
    class Meta: model = BookingOffer


# Inline models resources (Commercial)
class CommercialWelcomeToResource(resources.ModelResource):
    class Meta: model = CommercialWelcomeTo

class CommercialLocationResource(resources.ModelResource):
    class Meta: model = CommercialLocation

class CommercialWebSliderResource(resources.ModelResource):
    class Meta: model = CommercialWebSlider

class CommercialOverviewResource(resources.ModelResource):
    class Meta: model = CommercialOverview

class CommercialAboutUsResource(resources.ModelResource):
    class Meta: model = CommercialAboutUs

class CommercialUSPResource(resources.ModelResource):
    class Meta: model = CommercialUSP

class CommercialConfigurationResource(resources.ModelResource):
    class Meta: model = CommercialConfiguration

class CommercialProjectAmenitiesResource(resources.ModelResource):
    class Meta: model = CommercialProjectAmenities

class CommercialGalleryResource(resources.ModelResource):
    class Meta: model = CommercialGallery

class CommercialHeaderResource(resources.ModelResource):
    class Meta: model = CommercialHeader

class CommercialRERAInfoResource(resources.ModelResource):
    class Meta: model = CommercialRERAInfo

class CommercialConnectivityResource(resources.ModelResource):
    class Meta: model = CommercialConnectivity

class CommercialWhyInvestResource(resources.ModelResource):
    class Meta: model = CommercialWhyInvest

class CommercialBookingOfferResource(resources.ModelResource):
    class Meta: model = CommercialBookingOffer

class CommercialBankOfferResource(resources.ModelResource):
    class Meta: model = CommercialBankOffer


# ----------------------------------------------------------------
# INLINE CLASSES (Residential)
# ----------------------------------------------------------------
class WelcomeToInline(admin.StackedInline): model = WelcomeTo; extra = 1
class LocationInline(admin.StackedInline): model = Location; extra = 1
class WebSliderInline(admin.StackedInline): model = WebSlider; extra = 3
class OverviewInline(admin.StackedInline): model = Overview; extra = 1
class AboutUsInline(admin.StackedInline): model = AboutUs; extra = 1
class USPInline(admin.StackedInline): model = USP; extra = 4
class ConfigurationInline(admin.StackedInline): model = Configuration; extra = 2
class Project_AmenitiesInline(admin.StackedInline): model = Project_Amenities; extra = 4
class GalleryInline(admin.StackedInline): model = Gallery; extra = 3
class HeaderInline(admin.StackedInline): model = Header; extra = 1
class RERA_InfoInline(admin.StackedInline): model = RERA_Info; extra = 1
class ConnectivityInline(admin.StackedInline): model = Connectivity; extra = 4
class WhyInvestInline(admin.StackedInline): model = WhyInvest; extra = 4
class BookingOfferInline(admin.StackedInline): model = BookingOffer; extra = 3


# ----------------------------------------------------------------
# RESIDENTIAL ADMIN
# ----------------------------------------------------------------
@admin_thumbnails.thumbnail('image')
class ResidentialAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ResidentialResource
    inlines = [
        WelcomeToInline, LocationInline, WebSliderInline, OverviewInline, AboutUsInline,
        USPInline, ConfigurationInline, Project_AmenitiesInline, GalleryInline,
        HeaderInline, RERA_InfoInline, ConnectivityInline, WhyInvestInline, BookingOfferInline,
    ]
    list_display = ['id','image_thumbnail','project_name','developer','active','featured_property',
        'locality','city','propert_type','possession_year']
    search_fields = ['project_name']
    list_filter = ['developer','active','featured_property','locality','city','propert_type','possession_year']

admin.site.register(Residential, ResidentialAdmin)


# ----------------------------------------------------------------
# INLINE CLASSES (Commercial)
# ----------------------------------------------------------------
class CommercialWelcomeToInline(admin.StackedInline): model = CommercialWelcomeTo; extra = 1
class CommercialLocationInline(admin.StackedInline): model = CommercialLocation; extra = 1
class CommercialWebSliderInline(admin.StackedInline): model = CommercialWebSlider; extra = 3
class CommercialOverviewInline(admin.StackedInline): model = CommercialOverview; extra = 1
class CommercialAboutUsInline(admin.StackedInline): model = CommercialAboutUs; extra = 1
class CommercialUSPInline(admin.StackedInline): model = CommercialUSP; extra = 4
class CommercialConfigurationInline(admin.StackedInline): model = CommercialConfiguration; extra = 2
class CommercialProjectAmenitiesInline(admin.StackedInline): model = CommercialProjectAmenities; extra = 4
class CommercialGalleryInline(admin.StackedInline): model = CommercialGallery; extra = 3
class CommercialHeaderInline(admin.StackedInline): model = CommercialHeader; extra = 1
class CommercialRERAInfoInline(admin.StackedInline): model = CommercialRERAInfo; extra = 1
class CommercialConnectivityInline(admin.StackedInline): model = CommercialConnectivity; extra = 4
class CommercialWhyInvestInline(admin.StackedInline): model = CommercialWhyInvest; extra = 4
class CommercialBookingOfferInline(admin.StackedInline): model = CommercialBookingOffer; extra = 3
class CommercialBankOfferInline(admin.StackedInline): model = CommercialBankOffer; extra = 2


# ----------------------------------------------------------------
# COMMERCIAL ADMIN
# ----------------------------------------------------------------
@admin_thumbnails.thumbnail('image')
class CommercialProjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CommercialProjectResource
    inlines = [
        CommercialWelcomeToInline, CommercialLocationInline, CommercialWebSliderInline,
        CommercialOverviewInline, CommercialAboutUsInline, CommercialUSPInline,
        CommercialConfigurationInline, CommercialProjectAmenitiesInline,
        CommercialGalleryInline, CommercialHeaderInline, CommercialRERAInfoInline,
        CommercialConnectivityInline, CommercialWhyInvestInline,
        CommercialBookingOfferInline, CommercialBankOfferInline,
    ]
    list_display = ['id','image_thumbnail','project_name','developer','active','featured_property',
        'locality','city','property_type','possession_year']
    search_fields = ['project_name']
    list_filter = ['developer','active','featured_property','locality','city','property_type','possession_year']

admin.site.register(CommercialProject, CommercialProjectAdmin)


# ----------------------------------------------------------------
# ENQUIRIES ADMIN
# ----------------------------------------------------------------
@admin.register(ResidentialEnquiry)
class ResidentialEnquiryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ResidentialEnquiryResource
    list_display = ('id','residential','name','email','phone','contacted_on')
    search_fields = ('name','email','phone','residential__project_name')
    list_filter = ('contacted_on','residential')

@admin.register(CommercialEnquiry)
class CommercialEnquiryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CommercialEnquiryResource
    list_display = ('id','commercial','name','email','phone','contacted_on')
    search_fields = ('name','email','phone','commercial__project_name')
    list_filter = ('contacted_on','commercial')


# ----------------------------------------------------------------
# REGISTER INLINE MODELS SEPARATELY FOR IMPORT/EXPORT
# ----------------------------------------------------------------
admin.site.register(WelcomeTo, type('WelcomeToAdmin',(ImportExportModelAdmin,),{'resource_class':WelcomeToResource}))
admin.site.register(Location, type('LocationAdmin',(ImportExportModelAdmin,),{'resource_class':LocationResource}))
admin.site.register(WebSlider, type('WebSliderAdmin',(ImportExportModelAdmin,),{'resource_class':WebSliderResource}))
admin.site.register(Overview, type('OverviewAdmin',(ImportExportModelAdmin,),{'resource_class':OverviewResource}))
admin.site.register(AboutUs, type('AboutUsAdmin',(ImportExportModelAdmin,),{'resource_class':AboutUsResource}))
admin.site.register(USP, type('USPAdmin',(ImportExportModelAdmin,),{'resource_class':USPResource}))
admin.site.register(Configuration, type('ConfigurationAdmin',(ImportExportModelAdmin,),{'resource_class':ConfigurationResource}))
admin.site.register(Project_Amenities, type('ProjectAmenitiesAdmin',(ImportExportModelAdmin,),{'resource_class':ProjectAmenitiesResource}))
admin.site.register(Gallery, type('GalleryAdmin',(ImportExportModelAdmin,),{'resource_class':GalleryResource}))
admin.site.register(Header, type('HeaderAdmin',(ImportExportModelAdmin,),{'resource_class':HeaderResource}))
admin.site.register(RERA_Info, type('RERAInfoAdmin',(ImportExportModelAdmin,),{'resource_class':RERAInfoResource}))
admin.site.register(Connectivity, type('ConnectivityAdmin',(ImportExportModelAdmin,),{'resource_class':ConnectivityResource}))
admin.site.register(WhyInvest, type('WhyInvestAdmin',(ImportExportModelAdmin,),{'resource_class':WhyInvestResource}))
admin.site.register(BookingOffer, type('BookingOfferAdmin',(ImportExportModelAdmin,),{'resource_class':BookingOfferResource}))

admin.site.register(CommercialWelcomeTo, type('CWelcomeToAdmin',(ImportExportModelAdmin,),{'resource_class':CommercialWelcomeToResource}))
admin.site.register(CommercialLocation, type('CLocationAdmin',(ImportExportModelAdmin,),{'resource_class':CommercialLocationResource}))
admin.site.register(CommercialWebSlider, type('CWebSliderAdmin',(ImportExportModelAdmin,),{'resource_class':CommercialWebSliderResource}))
admin.site.register(CommercialOverview, type('COverviewAdmin',(ImportExportModelAdmin,),{'resource_class':CommercialOverviewResource}))
admin.site.register(CommercialAboutUs, type('CAboutUsAdmin',(ImportExportModelAdmin,),{'resource_class':CommercialAboutUsResource}))
admin.site.register(CommercialUSP, type('CUSPAdmin',(ImportExportModelAdmin,),{'resource_class':CommercialUSPResource}))
admin.site.register(CommercialConfiguration, type('CConfigAdmin',(ImportExportModelAdmin,),{'resource_class':CommercialConfigurationResource}))
admin.site.register(CommercialProjectAmenities, type('CAmenitiesAdmin',(ImportExportModelAdmin,),{'resource_class':CommercialProjectAmenitiesResource}))
admin.site.register(CommercialGallery, type('CGalleryAdmin',(ImportExportModelAdmin,),{'resource_class':CommercialGalleryResource}))
admin.site.register(CommercialHeader, type('CHeaderAdmin',(ImportExportModelAdmin,),{'resource_class':CommercialHeaderResource}))
admin.site.register(CommercialRERAInfo, type('CReraAdmin',(ImportExportModelAdmin,),{'resource_class':CommercialRERAInfoResource}))
admin.site.register(CommercialConnectivity, type('CConnAdmin',(ImportExportModelAdmin,),{'resource_class':CommercialConnectivityResource}))
admin.site.register(CommercialWhyInvest, type('CWhyInvestAdmin',(ImportExportModelAdmin,),{'resource_class':CommercialWhyInvestResource}))
admin.site.register(CommercialBookingOffer, type('CBookingAdmin',(ImportExportModelAdmin,),{'resource_class':CommercialBookingOfferResource}))
admin.site.register(CommercialBankOffer, type('CBankAdmin',(ImportExportModelAdmin,),{'resource_class':CommercialBankOfferResource}))

import admin_thumbnails
from django.contrib import admin
from django.http import HttpResponse
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from mptt.admin import DraggableMPTTAdmin
from django.http import FileResponse
from .models import *
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import io
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from django.conf import settings
import os

# ✅ Register Hindi Font
pdfmetrics.registerFont(
    TTFont('NotoSansDevanagari', 'Makaan_Hub/fonts/NotoSansDevanagari-Regular.ttf')
)

# ----------------------------------------------------------------------
# RESOURCES for Import/Export
# ----------------------------------------------------------------------
class AgenciesResource(resources.ModelResource):
    class Meta:
        model = Agencies
        fields = (
            'id','agencies_name','agencies_type','find_from','address',
            'locality','city','contact_person','contact_no','description',
            'email','status','meeting_follow_up','slug',
            'create_at','update_at','created_by','updated_by'
        )
        export_order = fields

class FollowUpResource(resources.ModelResource):
    class Meta:
        model = Follow_Up
        fields = ('id','company','follow_up','comment','locality_city','create_at','update_at')
        export_order = fields

class MeetingResource(resources.ModelResource):
    class Meta:
        model = Meeting
        fields = ('id','company','meeting','comment','locality_city','create_at','update_at')
        export_order = fields

class VisitResource(resources.ModelResource):
    class Meta:
        model = Visit
        fields = ('id','company','visit_type','status','meet_by','description','followup_meeting','locality_city','create_at','update_at')
        export_order = fields

class MetaResponseResource(resources.ModelResource):
    class Meta:
        model = Meta_Response
        fields = (
            'id','name','contact_no','email_id','business_name','description',
            'meeting_follow_up','business_type','requirent_type','response_status',
            'call_status','locality_city','create_at','update_at','created_by','updated_by'
        )
        export_order = fields

class ResponeMeetingResource(resources.ModelResource):
    class Meta:
        model = Respone_Meeting
        fields = ('id','respone','comment','meeting','locality_city','create_at','update_at')
        export_order = fields

class ResponeFollowUpResource(resources.ModelResource):
    class Meta:
        model = ResponeFollowUp
        fields = ('id','respone','comment','follow_up','locality_city','create_at','update_at')
        export_order = fields

# ----------------------------------------------------------------------
# CUSTOM EXPORT ACTIONS (PDF)
# ----------------------------------------------------------------------
@admin.action(description='Download Meta Responses PDF')
def export_meta_response_pdf(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="meta_responses.pdf"'

    doc = SimpleDocTemplate(response, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()

    elements.append(Paragraph("📝 Meta Response Brochure", styles['Title']))
    elements.append(Spacer(1, 12))

    data = [['Sr. No.','ID','Name','Contact No','Email','Description']]

    for i, obj in enumerate(queryset, start=1):
        data.append([
            str(i),
            str(obj.id),
            getattr(obj,'name','') or '',
            getattr(obj,'contact_no','') or '',
            getattr(obj,'email_id','') or '',
            getattr(obj,'description','') or '',
        ])

    table = Table(data, repeatRows=1)
    table.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#4a90e2')),
        ('TEXTCOLOR',(0,0),(-1,0),colors.white),
        ('ALIGN',(0,0),(-1,-1),'LEFT'),
        ('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),
        ('FONTSIZE',(0,0),(-1,-1),6),
        ('BOTTOMPADDING',(0,0),(-1,0),6),
        ('BACKGROUND',(0,1),(-1,-1),colors.whitesmoke),
        ('GRID',(0,0),(-1,-1),0.3,colors.grey),
    ]))

    elements.append(table)
    doc.build(elements)
    return response

def export_agency_pdf(modeladmin, request, queryset):
    from io import BytesIO
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    y = height - inch

    p.setFont("NotoSansDevanagari", 12)
    count = 0
    serial = 1

    for agency in queryset:
        if count > 0 and count % 8 == 0:
            p.showPage()
            p.setFont("NotoSansDevanagari", 12)
            y = height - inch

        p.setFont("Helvetica-Bold", 12)
        p.drawString(25, y, f"क्रमांक: {serial}")
        y -= 20

        p.setFont("NotoSansDevanagari", 12)
        script_lines = [
            f"{agency.contact_no}",
            f"({agency.id}) ({agency.agencies_name}) से बात कर रहे हैं? मुझे आपका नंबर Net से मिला है।",
            f"{agency.address or 'N/A'}",
        ]
        for line in script_lines:
            if y < 100:
                p.showPage()
                p.setFont("NotoSansDevanagari", 10)
                y = height - inch
            p.drawString(25, y, line)
            y -= 18

        y -= 13
        count += 1
        serial += 1

    p.save()
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')

# ----------------------------------------------------------------------
# INLINES
# ----------------------------------------------------------------------
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

class Respone_MeetingInline(admin.TabularInline):
    model = Respone_Meeting
    extra = 1
    show_change_link = True

class ResponeFollowUpInline(admin.TabularInline):
    model = ResponeFollowUp
    extra = 1
    show_change_link = True

# ----------------------------------------------------------------------
# ADMINS with ImportExportModelAdmin
# ----------------------------------------------------------------------
@admin_thumbnails.thumbnail('image')
class AgenciesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = AgenciesResource
    list_display = ['id','agencies_name','address','contact_no','description','status',
        'contact_person','meeting_follow_up','image_thumbnail','email','city','locality',
        'create_at','update_at','find_from','agencies_type','created_by','updated_by']
    list_filter = ['create_at','city','locality','status','meeting_follow_up']
    search_fields = ['id','agencies_name','contact_person','contact_no','description','email']
    list_editable = ('meeting_follow_up','city','description','locality','status')
    list_per_page = 20
    actions = [export_agency_pdf]
    inlines = [Follow_UpInline, MeetingInline, VisitInline]
    readonly_fields = ('created_by','updated_by',)

    def save_model(self, request, obj, form, change):
        if not change and not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

class MeetingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = MeetingResource
    list_display = ['id','company','meeting','comment','create_at','update_at']    
    list_filter = ('meeting','create_at','update_at',) 
    list_per_page = 50 

class Follow_UpAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = FollowUpResource
    list_display = ['id','company','follow_up','comment','create_at','update_at']   
    list_filter = ('follow_up','create_at','update_at',) 
    list_per_page = 20 

class VisitAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = VisitResource
    list_display = ['id','visit_type','status','company','meet_by','description',
        'followup_meeting','create_at','update_at']   
    search_fields = ['company','description','meet_by']
    list_filter = ('followup_meeting','status','create_at','update_at') 
    list_per_page = 20 

class Meta_ResponseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = MetaResponseResource
    list_display = [
        'id','call_status','contact_no','description','name','email_id','business_name',
        'meeting_follow_up','business_type','requirent_type','response_status',
        'locality_city','create_at','update_at','created_by','updated_by'
    ]
    list_filter = ['meeting_follow_up','business_type','requirent_type','locality_city','call_status']
    search_fields = ['name','contact_no','email_id','business_name','description']
    list_editable = ('call_status',)
    list_per_page = 10
    inlines = [Respone_MeetingInline,ResponeFollowUpInline]
    readonly_fields = ('created_by','updated_by',)
    actions = [export_meta_response_pdf]

    def save_model(self, request, obj, form, change):
        if not change and not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

class Respone_MeetingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ResponeMeetingResource
    list_display = ['id','respone','comment','meeting','locality_city','create_at','update_at']    
    list_filter = ['locality_city','meeting']
    search_fields = ['id','comment']
    list_editable = ('comment','meeting','locality_city')
    list_per_page = 10

class ResponeFollowUpAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ResponeFollowUpResource
    list_display = ['id','respone','comment','follow_up','locality_city','create_at','update_at']    
    list_filter = ['locality_city','follow_up']
    search_fields = ['id','comment']
    list_editable = ('comment','follow_up','locality_city')
    list_per_page = 10

# ----------------------------------------------------------------------
# REGISTER MODELS
# ----------------------------------------------------------------------
admin.site.register(Agencies, AgenciesAdmin)
admin.site.register(Follow_Up, Follow_UpAdmin)
admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Visit, VisitAdmin)
admin.site.register(Meta_Response, Meta_ResponseAdmin)
admin.site.register(Respone_Meeting, Respone_MeetingAdmin)
admin.site.register(ResponeFollowUp, ResponeFollowUpAdmin)

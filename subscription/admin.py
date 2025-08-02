import admin_thumbnails
from django.contrib import admin
from django.http import HttpResponse

# Register your models here.
from mptt.admin import DraggableMPTTAdmin
from .models import *
from django.contrib import admin
from django.http import FileResponse
from .models import Agencies
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import io
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import ttfonts
from django.conf import settings
import os

pdfmetrics.registerFont(
    TTFont('NotoSansDevanagari', 'Makaan_Hub/fonts/NotoSansDevanagari-Regular.ttf')
)

@admin.action(description='Download Meta Responses PDF')
def export_meta_response_pdf(modeladmin, request, queryset):
    from django.http import HttpResponse
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
    from reportlab.lib.pagesizes import A4
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="meta_responses.pdf"'

    doc = SimpleDocTemplate(response, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()

    elements.append(Paragraph("📝 Meta Response Brochure", styles['Title']))
    elements.append(Spacer(1, 12))

    # Header Row with Serial No.
    data = [[
        'Sr. No.', 'ID', 'Name', 'Contact No', 'Business Name', 'Description',
    ]]

    # Data Rows with Serial Numbers
    for i, obj in enumerate(queryset, start=1):
        data.append([
            str(i),
            str(obj.id),
            getattr(obj, 'name', '') or '',
            getattr(obj, 'contact_no', '') or '',
            getattr(obj, 'email_id', '') or '',
            getattr(obj, 'description', '') or '',
        ])

    table = Table(data, repeatRows=1)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4a90e2')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 0.3, colors.grey),
    ]))

    elements.append(table)
    doc.build(elements)
    return response

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

def export_agency_pdf(modeladmin, request, queryset):
    from io import BytesIO
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import inch
    from django.http import HttpResponse

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    y = height - inch

    p.setFont("NotoSansDevanagari", 12)

    count = 0
    serial = 1  # Serial Number

    for agency in queryset:
        # Reset y if starting new page after every 3 results
        if count > 0 and count % 8 == 0:
            p.showPage()
            p.setFont("NotoSansDevanagari", 12)
            y = height - inch

        # Heading with Serial Number
        p.setFont("Helvetica-Bold", 12)
        p.drawString(25, y, f"क्रमांक: {serial}" "")
        y -= 20

        p.setFont("NotoSansDevanagari", 12)
        script_lines = [
            f"{agency.contact_no }",  
            f"({agency.id or 'N/A'})({agency.agencies_name or 'N/A'}) से बात कर रहे हैं? मुझे आपका नंबर Net से मिला है।",  
            f" ({agency.address or 'N/A'})",
        ]

        for line in script_lines:
            if y < 100:
                p.showPage()
                p.setFont("NotoSansDevanagari", 10)
                y = height - inch
            p.drawString(25, y, line)
            y -= 18

        y -= 13  # Space between agencies
        count += 1
        serial += 1

    p.save()
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')

@admin_thumbnails.thumbnail('image')
class AgenciesAdmin(admin.ModelAdmin):
    list_display = ['id','agencies_name','address','contact_no','description','status','contact_person','meeting_follow_up','image_thumbnail','email','city','locality','create_at','update_at','find_from','agencies_type','created_by','updated_by']
    list_filter = ['create_at','city','locality','status','meeting_follow_up']
    search_fields = ['id','agencies_name','contact_person','contact_no','description','email']
    list_editable = ('meeting_follow_up','city','description','locality','status')
    list_per_page = 20
    actions = [export_agency_pdf]
    inlines = [Follow_UpInline, MeetingInline, VisitInline]
    readonly_fields = ('created_by', 'updated_by',)

    def save_model(self, request, obj, form, change):
        if not change and not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)
    
class MeetingAdmin(admin.ModelAdmin):
    list_display = ['id','company', 'meeting','comment','create_at','update_at']    
    
    list_filter = ('meeting','create_at','update_at',) 
    list_per_page = 50 
class Follow_UpAdmin(admin.ModelAdmin):
    list_display = ['id', 'company', 'follow_up','comment', 'create_at','update_at']   
    
    list_filter = ('follow_up','create_at','update_at',) 
    list_per_page = 20 
class VisitAdmin(admin.ModelAdmin):
    list_display = ['id','visit_type', 'status', 'company', 'meet_by', 'description', 'followup_meeting','create_at','update_at']   
    search_fields = ['company', 'description','meet_by',]
    
    list_filter = ('followup_meeting','status', 'create_at','update_at',) 
    list_per_page = 20 
admin.site.register(Follow_Up,Follow_UpAdmin)
admin.site.register(Meeting,MeetingAdmin)
admin.site.register(Visit,VisitAdmin)
admin.site.register(Agencies,AgenciesAdmin)

class Respone_MeetingInline(admin.TabularInline):
    model = Respone_Meeting
    extra = 1
    show_change_link = True

class Meta_ResponseAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'contact_no', 'email_id', 'business_name', 'description',
        'meeting_follow_up', 'business_type', 'requirent_type', 'response_status',
        'call_status', 'locality_city', 'create_at', 'update_at', 'created_by','updated_by',
    ]
    list_filter = ['meeting_follow_up', 'business_type', 'requirent_type', 'locality_city', 'call_status']
    search_fields = ['name', 'contact_no', 'email_id', 'business_name', 'description']
    list_editable = ('call_status',)
    list_per_page = 10
    inlines = [Respone_MeetingInline]
    readonly_fields = ('created_by', 'updated_by',)

    actions = [export_meta_response_pdf]  # ✅ Add this line

    def save_model(self, request, obj, form, change):
        if not change and not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Meta_Response, Meta_ResponseAdmin)

class Respone_MeetingAdmin(admin.ModelAdmin):
    list_display = ['id','respone','comment','meeting','locality_city', 'create_at','update_at',]    
    
    list_filter = ['locality_city','meeting']
    search_fields = ['id','comment',]
    list_editable = ('comment','meeting', 'locality_city',)
    list_per_page = 50
    
admin.site.register(Respone_Meeting,Respone_MeetingAdmin)



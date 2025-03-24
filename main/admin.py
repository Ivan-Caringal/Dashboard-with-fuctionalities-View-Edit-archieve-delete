from django.contrib import admin
from django.utils.html import format_html
from .models import BarangayDetails 
from .models import BarangayFileReport 



# Register your models here.
class BarangayDetailsAdmin(admin.ModelAdmin):
    def population_info(self, obj):
        return format_html(
            '<strong>Total:</strong> {}<br>'
            '<span style="color:blue;">Male:</span> {} | '
            '<span style="color:purple;">Female:</span> {}',
            obj.total_population, obj.male_population, obj.female_population
        )
    population_info.short_description = "Population"
    # if display username
    def submitted_by(self, obj):
        return obj.user.username if obj.user else "No User"
    submitted_by.short_description = "Submitted By"

    # if display id
    #  def submitted_by(self, obj):
    #     return obj.user.id if obj.user else "No User"
    # submitted_by.short_description = "Submitted By User"

    list_display = ('id', 'name', 'captain', 'population_info', 'submitted_by')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'captain', 'user__username')
    list_filter = ('name', 'user')

admin.site.register(BarangayDetails, BarangayDetailsAdmin)


from django.contrib import admin
from django.utils.html import format_html
from .models import BarangayDetails, BarangayFileReport

class BarangayFileReportAdmin(admin.ModelAdmin):
    def attachment_preview(self, obj):
        if obj.attachments:
            return format_html(
                '<a href="{}" target="_blank">📄 View File</a>', obj.attachments.url
            )
        return "No Attachment"

    attachment_preview.short_description = "Attachment"
    def submitted_by(self, obj):
        return obj.user.username if obj.user else "No User"
    submitted_by.short_description = "Submitted By"

    list_display = ('id', 'resident_name', 'incident_type', 'severity_level', 'incident_date', 'approval_status', 'attachment_preview', 'submitted_by')
    list_display_links = ('id', 'resident_name')
    list_editable = ('approval_status',)
    search_fields = ('resident_name', 'incident_type', 'barangay_street', 'severity_level')
    list_filter = ('severity_level', 'incident_year', 'incident_month', 'approval_status')

    def incident_date(self, obj):
        return f"{obj.incident_year}-{obj.incident_month}-{obj.incident_day}"

    incident_date.short_description = "Incident Date"

admin.site.register(BarangayFileReport, BarangayFileReportAdmin)




from django.contrib import admin

# Register your models here.
from django.contrib.admin import AdminSite

from reports.models import report


class report_admin(admin.ModelAdmin):

    list_display = ('name_company', 'title', 'unified_number', 'upload','date')
    list_editable =( 'title', 'unified_number', 'upload','date')
    list_filter = ('name_company', 'title', 'unified_number')
    search_fields = ('name_company', 'title', 'unified_number','date')

admin.site.register(report,report_admin)


admin.sites.AdminSite.site_title = 'ادارة موقع فلك'


# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import Group,User


# Register your models here.
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field

from import_export import resources


from package.models import packages
from django.forms import TextInput, Textarea
from django.db import models






class package_resource(resources.ModelResource):
    name_pack = Field(attribute='name_pack', column_name='اسم الباقة')
    package_duration = Field(attribute='package_duration', column_name='مدة الباقة')
    price = Field(attribute='price', column_name='سعر الباقة')
    describtion = Field(attribute='describtion', column_name='وصف الباقة')





    class Meta:
        model = packages







class package_admin_excll(ImportExportModelAdmin,admin.ModelAdmin):
    formfield_overrides = {

        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 20})},
    }
    list_display = ('name_pack', 'package_duration', 'price', 'describtion')
    list_editable = ('package_duration', 'price', 'describtion')
    list_filter = ('price', 'package_duration')
    search_fields = ('price', 'package_duration', 'name_pack')

    resource_class = package_resource




admin.site.unregister(Group)

admin.site.register(packages,package_admin_excll)


admin.site.site_header="FALAK"





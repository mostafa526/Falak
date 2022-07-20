from django.contrib import admin

# Register your models here.
from django.contrib import admin


from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field

from import_export import resources
from company.models import companies

from django.forms import TextInput, Textarea
from django.db import models


class companies_resource(resources.ModelResource):
    name_company = Field(attribute='name_company', column_name='اسم المنشأة')
    num_company = Field(attribute='num_company' , column_name="رقم المنشأة")
    unified_national_number = Field(attribute='unified_national_number',column_name="الرقم الوطنى الموحد")

    num_selling_record = Field(attribute='num_selling_record',column_name="رقم ترخيص السجل التجارى")
    location_selling_record = Field(attribute='location_selling_record',column_name="مصدر ترخيص السجل التجارى")
    end_date_selling_record = Field(attribute='end_date_selling_record',column_name="تاريخ انتهاء ترخيص السجل التجارى")

    num_baladia_license = Field(attribute='num_baladia_license', column_name="رقم ترخيص البلدية")
    location_baladia_license = Field(attribute='location_baladia_license' ,column_name="مصدر ترخيص البلدية")
    end_date_baladia_license =Field(attribute='end_date_baladia_license', column_name="تاريخ انتهاء ترخيص البلدية")

    unified_number = Field(attribute='unified_number', column_name="الرقم الموحد")
    nationality_establishment = Field(attribute='nationality_establishment', column_name="جنسية المنشأة")
    date_founding = Field(attribute='date_founding', column_name="تاريخ بداية المنشأة")

    main = Field(attribute='main', column_name="رئيسى")
    city = Field(attribute='city',  column_name="المدينة")
    status = Field(attribute="status", column_name="الحالة")

    adress_national = Field(attribute='adress_national', column_name="العنوان الوطنى")
    phone = Field(attribute='phone',  column_name="التليفون")




    class Meta:
        model = companies






class companies_admin(ImportExportModelAdmin,admin.ModelAdmin):


    list_display = ('num_company','name_company','unified_national_number','status','num_selling_record','location_selling_record','num_baladia_license','location_baladia_license','unified_number','nationality_establishment','date_founding','adress_national','phone')

    list_editable = (['name_company','unified_national_number','status','num_selling_record','location_selling_record','num_baladia_license','location_baladia_license','unified_number','nationality_establishment','date_founding','adress_national','phone'])
    list_filter = ('num_company','name_company','unified_number','status')
    search_fields =('num_company','name_company','unified_number')
    resource_class = companies_resource




admin.site.register(companies,companies_admin)





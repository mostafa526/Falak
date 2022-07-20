from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from import_export.fields import Field

from import_export import resources
from import_export.widgets import ForeignKeyWidget,CharWidget
from package.models import packages
from clerks.models import clerk
from clerks.models import companies




class clerks_resource(resources.ModelResource):
    name = Field(attribute='name', column_name='اسم الموظف')
    number_subscribtion = Field(attribute='number_subscribtion', column_name="رقم الاشتراك")
    id_emp = Field(attribute='id_emp',column_name="رقم الهوية")
    phone = Field(attribute='phone',column_name="رقم الجوال")

    email = Field(attribute='email',column_name="البريد الالكترونى")
    iban = Field(attribute='iban',column_name="الايبان")

    start_date = Field(attribute='start_date', column_name="تاريخ الالتحاق")
    code_bank = Field(attribute='code_bank', column_name="رمز البنك")
    job_title =Field(attribute='job_title', column_name="المسمى الوظيفى")

    num_company = Field(attribute='num_company', column_name="المنشأة", widget=ForeignKeyWidget(companies, 'num_company'))
    subscriber_number = Field(attribute='subscriber_number', column_name="رقم المشترك")
    roles_pack = Field(attribute='roles_pack', column_name="حالة الباقة")

    roles_emp = Field(attribute='roles_emp', column_name="حالة الموظف")
    package_id = Field(attribute='package_id',  column_name="الباقة",   widget=ForeignKeyWidget(packages, 'name_pack'))




    class Meta:
        model = clerk









class import_ecport_clerck_admin(ImportExportModelAdmin,admin.ModelAdmin):



    list_display = ('id_emp','name','number_subscribtion','phone','email','iban','start_date','end_date','code_bank','company_name','num_company','job_title','subscriber_number','roles_pack','roles_emp','package_id')
    list_editable = (['number_subscribtion','phone','email','iban','start_date','code_bank','job_title','num_company','subscriber_number','roles_pack','roles_emp','package_id'])
    list_filter = ('package_id','num_company','roles_pack','roles_emp')
    search_fields =('name','id_emp','num_company__num_company','package_id__name_pack','num_company__name_company',)
    resource_class = clerks_resource


    def end_date(self,obj):

        from datetime import date






        package=obj.package_id.package_duration

        year=obj.start_date.year
        month = obj.start_date.month + package
        day=obj.start_date.day


        if month>12:
            year=obj.start_date.year+1
            month=month%12
            if (month==4 or month==6 or month==9 or month==11) and day>30:
                mydate = date(year, month, day-1)

            elif month==2 and day>28:
                day=28
                mydate = date(year, month, day)

            else:
                mydate = date(year, month, day)




        else:
            if (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
                mydate = date(year, month, day - 1)

            elif month == 2 and day > 28:
                day = 28
                mydate = date(year, month, day)

            else:
                mydate = date(year, month, day)


        return mydate
    end_date.short_description='تاريخ الانتهاء'


    def company_name(self,obj):
        name_company=obj.num_company.name_company


        return  name_company


    company_name.short_description='اسم المنشأة'



admin.site.register(clerk,import_ecport_clerck_admin)


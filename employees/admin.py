from django.contrib import admin


# Register your models here.
from import_export.admin import ImportExportModelAdmin

from import_export.fields import Field

from import_export import resources
from import_export.widgets import ForeignKeyWidget

from company.models import companies
from employees.models import employees_company




class employees_resource(resources.ModelResource):
    sub_data_emp = Field(attribute='sub_data_emp', column_name="بيانات الاشتراك فى مدد")
    name_emp = Field(attribute='name_emp' , column_name="اسم الموظف ")
    name_father_emp = Field(attribute='name_father_emp',column_name="اسم الاب")
    name_gfather_emp = Field(attribute='name_gfather_emp',column_name="اسم الجد")
    family = Field(attribute='family',column_name="اسم العائلة")
    roles = Field(attribute='roles',column_name="نوع الهوية")
    number_identity = Field(attribute='number_identity', column_name="رقم الهوية")
    typ_credit = Field(attribute='typ_credit' ,column_name="نوع الفيزا")
    nationality =Field(attribute='nationality', column_name="الجنسية")
    religion = Field(attribute='religion', column_name="الديانة")
    gender = Field(attribute='gender', column_name="الجنس ")
    birth_date = Field(attribute='birth_date', column_name="تاريخ الميلاد")
    disability = Field(attribute='disability', column_name="عجز")
    email = Field(attribute='email',  column_name="البريد الالكترونى")
    id_country = Field(attribute="id_country", column_name="رمز البلد")
    phone_number = Field(attribute='phone_number', column_name="رقم الجوال ")
    number_build = Field(attribute='number_build',  column_name="رقم المبنى")
    name_street = Field(attribute='name_street', column_name="اسم الشارع")
    name_center = Field(attribute='name_center', column_name="اسم الحى")
    country = Field(attribute='country', column_name="البلد")
    city = Field(attribute='city', column_name="المدينة")
    postal_code = Field(attribute='postal_code', column_name="الرمز البريدى")
    gradution = Field(attribute='gradution', column_name="المؤهل العلمى ")
    join_date = Field(attribute='join_date', column_name="تاريخ الالتحاق")
    type_employe = Field(attribute='type_employe', column_name="نوع التوظيف ")
    job_name = Field(attribute='job_name', column_name="المسمى الوظيفى")
    carrer_ladder = Field(attribute='carrer_ladder', column_name="السلم الوظيفى")
    status_job = Field(attribute='status_job', column_name="الحالة الوظيفية ")
    date_end_contract = Field(attribute='date_end_contract', column_name="تاريخ انهاء العقد ")
    name_supervisor = Field(attribute='name_supervisor', column_name="اسم المشرف")
    payment_method = Field(attribute='payment_method', column_name="طريقة الدفع ")
    iban = Field(attribute="iban", column_name="رقم الايبان ")
    basic_wage = Field(attribute='basic_wage', column_name="الاجر الاساسى")
    month_housing_instead = Field(attribute='month_housing_instead', column_name="بدل السكن الشهرى ")
    transport_instead = Field(attribute='transport_instead', column_name="بدل النقل")
    medical_insurance_date = Field(attribute='medical_insurance_date', column_name="تاريخ التامين الطبى")
    medical_insurance_end_date = Field(attribute='name_father_emp', column_name="تاريخ انتهاء التامين الطبى ")
    number_polecy_insurance = Field(attribute='number_polecy_insurance', column_name="رقم بوليصة التامين الطبى ")
    number_passoort = Field(attribute='number_passoort', column_name="رقم الجواز ")
    release_date_passport = Field(attribute='release_date_passport', column_name="تاريخ اصدار الجواز")
    end_date_passport = Field(attribute='end_date_passport', column_name="تاريخ انتهاء الجواز ")
    num_company = Field(attribute='num_company', column_name="المنشأة ",widget=ForeignKeyWidget(companies, 'num_company'))


    class Meta:
        model = employees_company







class employees_admin(ImportExportModelAdmin,admin.ModelAdmin):



    list_display = ('number_identity','name_emp','num_company','company_name','family','nationality','religion','gender','number_build','gradution','job_name','status_job','payment_method','iban','basic_wage','month_housing_instead','transport_instead')
    list_editable = (
    ['name_emp', 'num_company', 'religion', 'number_build', 'job_name', 'status_job',
     'payment_method', 'iban', 'basic_wage', 'month_housing_instead', 'transport_instead'])

    list_filter = ('num_company','status_job','gender')

    search_fields =('number_identity','num_company__num_company','num_company__name_company','family','nationality','religion','job_name','basic_wage')
    resource_class = employees_resource








    def company_name(self, obj):
        return obj.num_company.name_company

    company_name.short_description = 'اسم المنشأة'




admin.site.register(employees_company,employees_admin)






from django.db import models

from company.models import companies


class employees_company(models.Model):
    ROLES = (

        ('الهوية الوطنية', 'الهوية الوطنية'),
        ('الاقامة','الاقامة'),
        ('جواز السفر', 'جواز السفر'),

    )

    GENDER = (

        ('ذكر', 'ذكر'),
        ('انثى', 'انثى'),


    )

    payment = (

        ('تحويل مصرفى', 'تحويل مصرفى'),
        ('شيك', 'شيك'),
        ('نقدا', 'نقدا'),

    )


    sub_data_emp= models.CharField(max_length=50,null=True,blank=True,verbose_name="بيانات الاشتراك فى مدد")
    name_emp= models.CharField(max_length=100,null=True,blank=True,verbose_name="اسم الموظف")
    name_father_emp= models.CharField(max_length=100,null=True,blank=True,verbose_name="اسم الاب")
    name_gfather_emp= models.CharField(max_length=100,null=True,blank=True,verbose_name="اسم الجد")
    family= models.CharField(max_length=100,null=True,blank=True,verbose_name="اسم العائلة")
    roles = models.CharField(max_length=100, choices = ROLES, null=False,verbose_name="نوع الهوية")
    number_identity= models.PositiveIntegerField(primary_key=True,unique=True,null=False,verbose_name=" رقم الهوية")
    typ_credit= models.CharField(max_length=100,null=True,blank=True,verbose_name="نوع الفيزا")
    nationality= models.CharField(max_length=100,null=False,blank=False,verbose_name="الجنسية")
    religion=models.CharField(max_length=100,null=True,blank=True,verbose_name="الديانة")
    gender=models.CharField(max_length=50, choices = GENDER, null=False,verbose_name="الجنس")
    birth_date= models.CharField(max_length=200,null=True,blank=True,verbose_name="تاريخ الميلاد")
    disability=models.CharField(max_length=50,null=True,blank=True,verbose_name="عجز")
    email=models.EmailField(null=True,blank=True,verbose_name="البريد الالكترونى")
    id_country=models.CharField(max_length=100,null=True,blank=True,verbose_name="رمز البلد")
    phone_number=models.CharField(max_length=100,null=True,blank=True,verbose_name="رقم الجوال")
    number_build=models.CharField(max_length=100,null=True,blank=True,verbose_name="رقم المبنى")
    name_street=models.CharField(max_length=20,null=True,blank=True,verbose_name="اسم الشارع")
    name_center=models.CharField(max_length=20,null=True,blank=True,verbose_name="اسم الحى")
    country=models.CharField(max_length=20,null=True,blank=True,verbose_name="البلد")
    city=models.CharField(max_length=20,null=True,blank=True,verbose_name="المدينة")
    postal_code=models.CharField(max_length=5,null=True,blank=True,verbose_name="الرمز البريدى")
    gradution=models.CharField(max_length=50,null=True,blank=True,verbose_name="المؤهل العلمى")
    join_date=models.CharField(max_length=50,null=True,blank=True,verbose_name="تاريخ الالتحاق")
    type_employe=models.CharField(max_length=200,null=True,blank=True,verbose_name="نوع التوظيف")
    job_name=models.CharField(max_length=200,null=True,blank=True,verbose_name="المسمى الوظيفى")
    carrer_ladder=models.CharField(max_length=200,null=True,blank=True,verbose_name="السلم الوظيفى")
    status_job=models.CharField(max_length=200,null=False,default='نشط',verbose_name="الحالة الوظيفية")
    date_end_contract=models.CharField(max_length=200,null=True,blank=True,verbose_name='تاريخ انهاء العقد')
    name_supervisor=models.CharField(max_length=300,null=True,blank=True,verbose_name='اسم المشرف')
    payment_method=models.CharField(max_length=100,choices=payment,blank=True,null=True,verbose_name='طريقة الدفع')
    iban=models.CharField(max_length=300,null=True,blank=True,verbose_name='رقم الايبان')
    basic_wage=models.IntegerField(max_length=10,null=False,verbose_name='الاجر الاساسى')
    month_housing_instead=models.IntegerField(max_length=10,null=False,verbose_name='بدل السكن الشهرى')
    transport_instead=models.IntegerField(max_length=10,null=False,verbose_name='بدل النقل')
    medical_insurance_date= models.CharField(max_length=200,null=True,blank=True,verbose_name="تاريخ التامين الطبى")
    medical_insurance_end_date= models.CharField(max_length=200,null=True,blank=True,verbose_name="تاريخ انتهاء التامين الطبى")
    number_polecy_insurance= models.CharField(max_length=200,null=True,blank=True,verbose_name="رقم بوليصة التامين الطبى")
    number_passoort= models.CharField(max_length=200,null=True,blank=True,verbose_name="رقم الجواز")
    release_date_passport= models.CharField(max_length=200,null=True,blank=True,verbose_name="تاريخ اصدار الجواز")
    end_date_passport= models.CharField(max_length=200,null=True,blank=True,verbose_name="تاريخ انتهاء الجواز")
    num_company= models.ForeignKey(companies,related_name='num_orgnizations',on_delete=models.CASCADE,null=False,verbose_name="المنشأة")















    class Meta:
        verbose_name = " موظفون المنشآت"

        verbose_name_plural = "موظفون المنشآت"
    def __str__(self):
        return self.name_emp










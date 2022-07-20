from django.db import models

# Create your models here.
from django.db import models

from company.models import companies
from package.models import packages



class clerk(models.Model):
    roles_emloyee = (

        ('سارى', 'سارى'),
        ('ملغى من قبل المنشأة', 'ملغى من قبل المنشأة'),
        ('فى انتظار موافقة الموظف', 'فى انتظار موافقة الموظف'),

    )

    roles_package = (

        ('نشط', 'نشط'),
        ('غير نشط', 'غير نشط'),

    )

    name= models.CharField(max_length=200,null=False,verbose_name="اسم الموظف")
    number_subscribtion= models.CharField(max_length=200,null=True,blank=True,verbose_name="رقم الاشتراك")
    id_emp= models.PositiveIntegerField(unique=True,null=False,verbose_name=" رقم الهوية",primary_key=True)
    phone= models.PositiveIntegerField(unique=True,max_length=300,null=True,blank=True,verbose_name="رقم الجوال")
    email= models.EmailField(unique=True,null=True,blank=True,verbose_name="البريد الالكترونى")
    iban= models.CharField(max_length=200,null=False,unique=True,verbose_name="الايبان")
    start_date= models.DateField(verbose_name='تاريخ الالتحاق', null=False)

    code_bank= models.CharField(max_length=50,null=True,blank=True,verbose_name="رمز البنك")
    job_title=models.CharField(max_length=100,null=True,blank=True,verbose_name='المسمى الوظيفى')
    num_company= models.ForeignKey(companies,related_name='nm_company',on_delete=models.CASCADE,null=False,verbose_name="المنشأة")

    subscriber_number=models.CharField(max_length=200,null=True,blank=True,verbose_name="رقم المشترك")
    roles_pack = models.CharField(max_length=50, choices = roles_package, null=False,verbose_name="حالة الباقة")
    roles_emp = models.CharField(max_length=50, choices = roles_emloyee, null=False,verbose_name="حالة الموظف")





    package_id= models.ForeignKey(packages,related_name='nm_package',on_delete=models.CASCADE,null=False,verbose_name="الباقة")
    delta=0


    class Meta:
        verbose_name = "الموظفون"

        verbose_name_plural = "الموظفون"

    def end_date_one(self):
        from datetime import date


        year = self.start_date.year
        month = self.start_date.month + 3
        day = self.start_date.day

        if month > 12:
            year = self.start_date.year + 1
            month = month % 12
            if (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
                mydate = date(year, month, day - 1)

            elif month == 2 and day > 28:
                day = 28
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
        self.wwwww = mydate

        return mydate

    def end_date_tow(self):
        from datetime import date

        year = self.start_date.year
        month = self.start_date.month + 6
        day = self.start_date.day

        if month > 12:
            year = self.start_date.year + 1
            month = month % 12
            if (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
                mydate = date(year, month, day - 1)

            elif month == 2 and day > 28:
                day = 28
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
        self.wwwww = mydate

        return mydate

    def end_date_three(self):
        from datetime import date

        year = self.start_date.year
        month = self.start_date.month + 9
        day = self.start_date.day

        if month > 12:
            year = self.start_date.year + 1
            month = month % 12
            if (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
                mydate = date(year, month, day - 1)

            elif month == 2 and day > 28:
                day = 28
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
        self.wwwww = mydate

        return mydate

    def end_date(self):
        from datetime import date

        package=self.package_id.package_duration


        year = self.start_date.year
        month = self.start_date.month + package
        day = self.start_date.day

        if month > 12:
            year = self.start_date.year + 1
            month = month % 12
            if (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
                mydate = date(year, month, day - 1)

            elif month == 2 and day > 28:
                day = 28
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
        self.wwwww = mydate

        return mydate








    def __int__(self):


        return self.id_emp




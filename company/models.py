
from django.db import models







class companies(models.Model):
    name_company= models.CharField(max_length=100,null=False,verbose_name="اسم المنشأة")
    num_company= models.CharField(max_length=100,null=False,verbose_name="رقم المنشأة",primary_key=True)
    unified_national_number=models.CharField(max_length=50,unique=True,null=False,verbose_name="الرقم الوطنى الموحد")



    num_selling_record=models.CharField(max_length=200,null=False,verbose_name="رقم ترخيص السجل التجارى")
    location_selling_record=models.CharField(max_length=200,null=True,blank=True,verbose_name="مصدر ترخيص السجل التجارى")
    end_date_selling_record=models.CharField(max_length=200,null=True,blank=True,verbose_name="تاريخ انتهاء ترخيص السجل التجارى")

    num_baladia_license= models.CharField(max_length=200, null=True,blank=True, verbose_name="رقم ترخيص البلدية")
    location_baladia_license= models.CharField(max_length=200, null=True,blank=True, verbose_name="مصدر ترخيص البلدية")
    end_date_baladia_license= models.CharField(max_length=200, null=True,blank=True, verbose_name="تاريخ انتهاء ترخيص البلدية")

    unified_number = models.CharField(max_length=100, null=True,blank=True, verbose_name="الرقم الموحد")
    nationality_establishment = models.CharField(max_length=50, null=False, verbose_name="جنسية المنشأة")
    date_founding = models.CharField(max_length=100, null=False, verbose_name="تاريخ بداية المنشأة")



    main = models.CharField(max_length=50, null=True,blank=True, verbose_name="رئيسى")
    city = models.CharField(max_length=50, null=True,blank=True, verbose_name="المدينة")
    status = models.CharField(max_length=50, null=False, verbose_name="الحالة")

    adress_national= models.CharField(max_length=100, null=True,blank=True, verbose_name="العنوان الوطنى")
    phone= models.CharField(max_length=100, null=True,blank=True, verbose_name="التليفون")




    class Meta:
        verbose_name = "المنشآت"

        verbose_name_plural = "المنشآت"




    def __str__(self):
        return self.num_company









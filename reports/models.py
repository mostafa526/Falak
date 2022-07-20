from django.db import models

# Create your models here.
class report(models.Model):

    name_company= models.CharField(max_length=100,null=False,verbose_name="اسم المنشأة")
    title= models.CharField(max_length=100,null=True,blank=True,verbose_name="عنوان التقرير")
    unified_number = models.CharField(max_length=100, null=False,blank=False, verbose_name="الرقم الموحد")
    upload = models.FileField(upload_to ='uploads/',verbose_name="التقرير")



    date= models.DateField(verbose_name='التاريخ', null=True,blank=True)




    class Meta:
        verbose_name = "التقارير"

        verbose_name_plural = "التقارير"


    def __str__(self):
        return self.unified_number
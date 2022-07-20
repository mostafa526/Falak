from django.db import models

# Create your models here.
class task(models.Model):
    title_task= models.CharField(max_length=400,null=False,blank=False,verbose_name="عنوان المهمة")
    employee_name= models.CharField(max_length=400,null=True,blank=True,verbose_name="الموظف",)
    path=models.CharField(max_length=400,blank=True,null=True,verbose_name="المسار")
    company=models.CharField(max_length=400,null=True,blank=True,verbose_name="المنصة")
    start_date= models.DateField(verbose_name='تاريخ بداية المهمة', null=True,blank=True)
    end_date= models.DateField(verbose_name='تاريخ نهاية  المهمة', null=True,blank=True)
    describtion=models.TextField(blank=True,null=True,verbose_name='وصف المهمة')
    upload = models.FileField(blank=True,null=True,upload_to ='uploads_taska/',verbose_name="المرفقات")

    class Meta:
        verbose_name = "المهمات"

        verbose_name_plural = "المهمات"


    def __str__(self):
        return self.title_task








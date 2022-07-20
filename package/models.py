
# Create your models here.

from django.db import models

# Create your models here.


class packages(models.Model):
    name_pack= models.CharField(max_length=100,null=False,verbose_name="نوع الباقة",primary_key=True)
    package_duration= models.PositiveIntegerField(null=False,verbose_name="مدة الباقة")
    price=models.FloatField(null=False,verbose_name="سعر الباقة")
    describtion=models.TextField(blank=True,null=True,verbose_name='وصف الباقة')

    class Meta:
        verbose_name = "الباقات"

        verbose_name_plural = "الباقات"


    def __str__(self):
        return self.name_pack

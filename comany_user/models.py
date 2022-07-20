from django.db import models
from django.conf import settings
# Create your models here.
class MyUser(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, related_name='user_company', on_delete=models.CASCADE)
    number_company = models.CharField(max_length=400,null=False,blank=False,verbose_name='الرقم الوطنى')



    class Meta:
        verbose_name = "مستخدمون المنشات"

        verbose_name_plural ="مستخدمون المنشات"


    def __str__(self):
        return self.user.username

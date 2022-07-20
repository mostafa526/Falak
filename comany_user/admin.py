from django.contrib import admin

# Register your models here.
from comany_user.models import MyUser

admin.site.register(MyUser)

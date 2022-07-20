from django.contrib import admin

# Register your models here.
from tasks.models import task


class task_admin(admin.ModelAdmin):

    list_display = ('title_task', 'employee_name', 'path', 'company','start_date','end_date','describtion','upload')
    list_editable =('employee_name', 'path', 'company','start_date','end_date','describtion','upload')
    list_filter = ('employee_name','company')
    search_fields =('employee_name','company','start_date','end_date')

admin.site.register(task,task_admin)
from django.contrib import admin
from .models import Employee, Leave
from django.contrib.auth.models import Group


admin.site.register(Employee)

class LeaveAdmin(admin.ModelAdmin):
    readonly_fields = ('employee','leave_type','leave_date','return_date','comment')

admin.site.register(Leave, LeaveAdmin)
admin.site.unregister(Group)


admin.site.site_header = 'EAX'                    
admin.site.index_title = 'EAX '                
admin.site.site_title = 'EAX'

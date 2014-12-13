from .models import *
from django.contrib import admin

class membersAdmin(admin.ModelAdmin):
	list_display = ['user_id','username','email_id','date_time']
	list_filter = ['date_time']
	search_fields = ['date_time']
	class Meta:
		model = members
class roleAdmin(admin.ModelAdmin):
	list_display = ['rolename']
	class Meta:
		model = role

admin.site.register(members,membersAdmin)
admin.site.register(role,roleAdmin)

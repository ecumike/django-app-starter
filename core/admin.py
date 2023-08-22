from django.contrib import admin

from .models import ErrorLog


@admin.register(ErrorLog)
class ErrorLogAdmin(admin.ModelAdmin):
	list_display = (
		'id',
		'created_at',
		'user',
		'url',
		'referer',
		'error_code',
		'error_message',
	)
	list_filter = ('created_at',)
	date_hierarchy = 'created_at'
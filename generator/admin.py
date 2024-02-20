from django.contrib import admin
from .models import SerialNumber

class SerialNumberAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'min_bulk_id', 'max_bulk_id', 'created_at', 'serial_number', 'qr_code_path']

admin.site.register(SerialNumber, SerialNumberAdmin)

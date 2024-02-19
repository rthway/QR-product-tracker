# # generator/admin.py
# from django.contrib import admin
# from .models import SerialNumber

# class SerialNumberAdmin(admin.ModelAdmin):
#     list_display = ('product_name', 'min_bulk_id', 'max_bulk_id', 'created_at')
#     search_fields = ['product_name']
#     list_filter = ['product_name']

# admin.site.register(SerialNumber, SerialNumberAdmin)
# generator/admin.py
# from django.contrib import admin
# from .models import SerialNumber
# import qrcode
# from django.utils.html import format_html

# class SerialNumberAdmin(admin.ModelAdmin):
#     list_display = ('product_name', 'min_bulk_id', 'max_bulk_id', 'created_at', 'serial_number_with_qr')
#     search_fields = ['product_name']
#     list_filter = ['product_name']

#     def serial_number_with_qr(self, obj):
#         factory_id = "01"
#         lots = obj.created_at.strftime("%y%m%d")
#         bundle_id = f"{obj.min_bulk_id}_{obj.max_bulk_id}"
#         serial_numbers_with_qr = []
        
#         for i in range(obj.min_bulk_id, obj.max_bulk_id + 1):
#             serial_number = f"{factory_id}{lots}{bundle_id}{i}"
#             qr_file_name = f"static/qr_codes/{serial_number}.png"
#             qr = qrcode.QRCode(
#                 version=1,
#                 error_correction=qrcode.constants.ERROR_CORRECT_L,
#                 box_size=10,
#                 border=4,
#             )
#             qr.add_data(serial_number)
#             qr.make(fit=True)
#             qr_img = qr.make_image(fill_color="black", back_color="white")
#             qr_img.save(qr_file_name)
#             serial_numbers_with_qr.append((serial_number, qr_file_name))
        
#         return format_html('<img src="{}" style="width: 100px; height: 100px;" />', serial_numbers_with_qr[0][1])

#     serial_number_with_qr.short_description = 'Serial Number with QR Code'

# admin.site.register(SerialNumber, SerialNumberAdmin)
# generator/admin.py
from django.contrib import admin
from .models import SerialNumber

class SerialNumberAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'min_bulk_id', 'max_bulk_id', 'serial_numbers_display', 'created_at')
    search_fields = ['product_name']
    list_filter = ['product_name']

    def serial_numbers_display(self, obj):
        return ', '.join([str(sn) for sn in obj.generate_serial_numbers()])
    serial_numbers_display.short_description = 'Serial Numbers'

admin.site.register(SerialNumber, SerialNumberAdmin)

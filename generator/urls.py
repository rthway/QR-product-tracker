from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_serial_numbers, name='generate_serial_numbers'),
    path('',views.view_generated_serial_numbers,name='view_qr_code'),
    path('print_qr_code/<str:bundle_number>/', views.print_qr_code, name='print_qr_code'),
    # Other URL patterns
]


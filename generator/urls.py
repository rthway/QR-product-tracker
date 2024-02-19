from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_serial_numbers, name='generate_serial_numbers'),
    path('',views.view_generated_serial_numbers,name='view_qr_code')
]

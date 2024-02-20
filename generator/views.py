# generator/views.py
from django.shortcuts import render
from .models import SerialNumber
import qrcode
from django.http import HttpResponse
from io import BytesIO

def print_qr_code(request, bundle_number):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(bundle_number)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img_io = BytesIO()
    img.save(img_io, format='PNG')
    img_io.seek(0)

    response = HttpResponse(img_io, content_type='image/png')
    response['Content-Disposition'] = 'inline; filename="qrcode.png"'
    return response
def generate_serial_numbers(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        min_bulk_id = int(request.POST.get('min_bulk_id'))
        max_bulk_id = int(request.POST.get('max_bulk_id'))
        serial_numbers = SerialNumber(product_name=product_name, min_bulk_id=min_bulk_id, max_bulk_id=max_bulk_id)
        serial_numbers.save()
        generated_serial_numbers = serial_numbers.generate_serial_numbers()
        return render(request, 'serial_numbers.html', {'serial_numbers': generated_serial_numbers, 'product_name':product_name, 'bundle_id' :f"{min_bulk_id}_{max_bulk_id}"})
    return render(request, 'generate_serial_numbers.html')

def  view_generated_serial_numbers(request):
    serial_numbers = SerialNumber.objects.all()
    for serial_number in serial_numbers:
        serial_number.bundle_number = serial_number.serial_number[:19]
    return  render(request, 'qr_code_list.html', {'serial_numbers': serial_numbers})

# generator/views.py
from django.shortcuts import render
from .models import SerialNumber

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
    return  render(request, 'qr_code_list.html', {'serial_numbers': serial_numbers})

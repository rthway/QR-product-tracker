# generator/models.py
from django.db import models
from datetime import datetime
import qrcode

class SerialNumber(models.Model):
    product_name = models.CharField(max_length=100)
    min_bulk_id = models.IntegerField()
    max_bulk_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_serial_numbers(self):
        serial_numbers_with_qr = []
        factory_id = "01"
        lots = datetime.now().strftime("%y%m%d")
        bundle_id = f"{self.min_bulk_id}_{self.max_bulk_id}"

        for i in range(self.min_bulk_id, self.max_bulk_id + 1):
            serial_number = f"{factory_id}{lots}{bundle_id}{i}"
            # Generate QR code for the serial number
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(serial_number)
            qr.make(fit=True)
            qr_img = qr.make_image(fill_color="black", back_color="white")
            # Save QR code image
            qr_file_name = f"static/qr_codes/{serial_number}.png"
            qr_img.save(qr_file_name)
            # Append serial number along with QR code file name
            serial_numbers_with_qr.append((serial_number, qr_file_name))

        return serial_numbers_with_qr
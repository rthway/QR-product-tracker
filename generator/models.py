
# # generator/models.py
# from django.db import models
# from datetime import datetime
# import qrcode

# class SerialNumber(models.Model):
#     product_name = models.CharField(max_length=100)
#     product_id = models.IntegerField(default=1)  # Added product_id field with a default value
#     min_bulk_id = models.IntegerField()
#     max_bulk_id = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     serial_number = models.CharField(max_length=255, null=True)  # Field to store serial numbers
#     qr_code_path = models.CharField(max_length=255, null=True)   # Allow null for qr_code_path temporarily

#     def generate_serial_numbers(self):
#         serial_numbers_with_qr = []
#         factory_id = "01"
#         lots = datetime.now().strftime("%y%m%d")
#         bundle_id = f"{self.min_bulk_id}_{self.max_bulk_id}"

#         for i in range(self.min_bulk_id, self.max_bulk_id + 1):
#             serial_number = f"{factory_id}{lots}{bundle_id}{i}"
#             # Generate QR code for the serial number
#             qr = qrcode.QRCode(
#                 version=1,
#                 error_correction=qrcode.constants.ERROR_CORRECT_L,
#                 box_size=10,
#                 border=4,
#             )
#             qr.add_data(serial_number)
#             qr.make(fit=True)
#             qr_img = qr.make_image(fill_color="black", back_color="white")
#             # Save QR code image
#             qr_file_name = f"static/qr_codes/{serial_number}.png"
#             qr_img.save(qr_file_name)
#             # Append serial number along with QR code file name
#             serial_numbers_with_qr.append((serial_number, qr_file_name))
#             # Store serial number and QR code path in database
#             self.serial_number = serial_number
#             self.qr_code_path = qr_file_name
#             self.save()

#         return serial_numbers_with_qr


# # generator/models.py
# from django.db import models
# from datetime import datetime
# import qrcode

# class SerialNumber(models.Model):
#     product_name = models.CharField(max_length=100)
#     product_id = models.IntegerField(default=1)  # Added product_id field with a default value
#     min_bulk_id = models.IntegerField()
#     max_bulk_id = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     serial_number = models.CharField(max_length=255)
#     qr_code_path = models.CharField(max_length=255)

#     def generate_serial_numbers(self):
#         factory_id = "01"
#         lots = datetime.now().strftime("%y%m%d")
#         bundle_id = f"{self.min_bulk_id}_{self.max_bulk_id}"

#         serial_numbers_with_qr = []

#         for i in range(self.min_bulk_id, self.max_bulk_id + 1):
#             serial_number = f"{factory_id}{lots}{bundle_id}{i}"
#             # Generate QR code for the serial number
#             qr = qrcode.QRCode(
#                 version=1,
#                 error_correction=qrcode.constants.ERROR_CORRECT_L,
#                 box_size=10,
#                 border=4,
#             )
#             qr.add_data(serial_number)
#             qr.make(fit=True)
#             qr_img = qr.make_image(fill_color="black", back_color="white")
#             # Save QR code image
#             qr_file_name = f"static/qr_codes/{serial_number}.png"
#             qr_img.save(qr_file_name)
#             # Append serial number along with QR code file name
#             serial_numbers_with_qr.append((serial_number, qr_file_name))

#         # Save all generated serial numbers and QR code paths to the database
#         for serial_number, qr_code_path in serial_numbers_with_qr:
#             SerialNumber.objects.create(
#                 product_name=self.product_name,
#                 product_id=self.product_id,
#                 min_bulk_id=self.min_bulk_id,
#                 max_bulk_id=self.max_bulk_id,
#                 created_at=self.created_at,
#                 serial_number=serial_number,
#                 qr_code_path=qr_code_path
#             )

#         return serial_numbers_with_qr
# # generator/models.py
# from django.db import models
# from datetime import datetime
# import qrcode

# class SerialNumber(models.Model):
#     product_name = models.CharField(max_length=100)
#     product_id = models.IntegerField(default=1)  # Added product_id field with a default value
#     min_bulk_id = models.IntegerField()
#     max_bulk_id = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     serial_number = models.CharField(max_length=255,unique=True)
#     qr_code_path = models.CharField(max_length=255)

#     def generate_serial_numbers(self):
#         factory_id = "01"
#         lots = datetime.now().strftime("%y%m%d")
#         bundle_id = f"{self.min_bulk_id}_{self.max_bulk_id}"

#         serial_numbers_with_qr = []

#         # Ensure min_bulk_id is less than or equal to max_bulk_id
#         if self.min_bulk_id <= self.max_bulk_id:
#             #print(f"Generating serial numbers from {self.min_bulk_id} to {self.max_bulk_id}")
#             for i in range(self.min_bulk_id, self.max_bulk_id + 1):
#                 serial_number = f"{factory_id}{lots}{bundle_id}{i}"
#                 # Generate QR code for the serial number
#                 qr = qrcode.QRCode(
#                     version=1,
#                     error_correction=qrcode.constants.ERROR_CORRECT_L,
#                     box_size=10,
#                     border=4,
#                 )
#                 qr.add_data(serial_number)
#                 qr.make(fit=True)
#                 qr_img = qr.make_image(fill_color="black", back_color="white")
#                 # Save QR code image
#                 qr_file_name = f"static/qr_codes/{serial_number}.png"
#                 qr_img.save(qr_file_name)
#                 # Append serial number along with QR code file name
#                 serial_numbers_with_qr.append((serial_number, qr_file_name))
          

#             # Save all generated serial numbers and QR code paths to the database
     
#             for serial_number, qr_code_path in serial_numbers_with_qr:
#                 SerialNumber.objects.create(
#                     product_name=self.product_name,
#                     product_id=self.product_id,
#                     min_bulk_id=self.min_bulk_id,
#                     max_bulk_id=self.max_bulk_id,
#                     created_at=self.created_at,
#                     serial_number=serial_number,
#                     qr_code_path=qr_code_path
#                 )


#         return serial_numbers_with_qr

# generator/models.py
from django.db import models
from datetime import datetime
import qrcode

class SerialNumber(models.Model):
    product_name = models.CharField(max_length=100)
    product_id = models.IntegerField(default=1)  # Added product_id field with a default value
    min_bulk_id = models.IntegerField()
    max_bulk_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    serial_number = models.CharField(max_length=255)
    qr_code_path = models.CharField(max_length=255)

    def generate_serial_numbers(self):
        factory_id = "01"
        lots = datetime.now().strftime("%y%m%d")
        bundle_id = f"{self.min_bulk_id}_{self.max_bulk_id}"

        serial_numbers_with_qr = []

        # Ensure min_bulk_id is less than or equal to max_bulk_id
        if self.min_bulk_id <= self.max_bulk_id:
            print(f"Generating serial numbers from {self.min_bulk_id} to {self.max_bulk_id}")
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

            # Save all generated serial numbers and QR code paths to the database
            for serial_number, qr_code_path in serial_numbers_with_qr:
                serial_obj = SerialNumber.objects.create(
                    product_name=self.product_name,
                    product_id=self.product_id,
                    min_bulk_id=self.min_bulk_id,
                    max_bulk_id=self.max_bulk_id,
                    created_at=self.created_at,
                    serial_number=serial_number,
                    qr_code_path=qr_code_path
                )
                serial_obj.save()

        return serial_numbers_with_qr

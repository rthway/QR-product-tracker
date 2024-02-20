# Generated by Django 5.0.2 on 2024-02-19 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='serialnumber',
            name='product_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='serialnumber',
            name='qr_code_path',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='serialnumber',
            name='serial_number',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

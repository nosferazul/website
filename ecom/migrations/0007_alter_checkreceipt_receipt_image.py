# Generated by Django 4.1 on 2023-05-04 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0006_checkreceipt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkreceipt',
            name='receipt_image',
            field=models.ImageField(upload_to='receipt_image'),
        ),
    ]

# Generated by Django 5.0.2 on 2024-03-05 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAlmacen', '0003_producto_descuento_porcentaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes'),
        ),
    ]

# Generated by Django 5.0.2 on 2024-03-05 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAlmacen', '0002_producto_oferta_alter_cliente_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descuento_porcentaje',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
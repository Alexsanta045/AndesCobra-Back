# Generated by Django 5.0.7 on 2024-12-09 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='obligaciones',
            old_name='fecha_facturazion_obligaion',
            new_name='fecha_facturacion_obligacion',
        ),
    ]

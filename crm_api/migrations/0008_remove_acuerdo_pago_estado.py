# Generated by Django 5.0.7 on 2025-01-07 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("crm_api", "0007_remove_acuerdo_pago_usuario_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="acuerdo_pago",
            name="estado",
        ),
    ]

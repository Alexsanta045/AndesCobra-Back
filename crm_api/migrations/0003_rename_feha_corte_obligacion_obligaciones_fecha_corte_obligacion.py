# Generated by Django 5.0.7 on 2024-12-09 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("crm_api", "0002_rename_estado_operaional_obligaciones_estado_operacional"),
    ]

    operations = [
        migrations.RenameField(
            model_name="obligaciones",
            old_name="feha_corte_obligacion",
            new_name="fecha_corte_obligacion",
        ),
    ]
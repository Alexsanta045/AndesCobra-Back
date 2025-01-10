# Generated by Django 5.0.7 on 2025-01-08 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crm_api", "0011_alter_acuerdo_pago_codigo_asesor"),
    ]

    operations = [
        migrations.CreateModel(
            name="Subir_pagos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("valor_pago", models.FloatField()),
                ("fecha_pago", models.DateField()),
                ("codigo", models.CharField(max_length=30)),
            ],
        ),
    ]

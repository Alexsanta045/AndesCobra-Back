# Generated by Django 5.0.7 on 2025-01-07 17:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crm_api", "0006_acuerdo_pago_codigo_asesor_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="acuerdo_pago",
            name="usuario",
        ),
        migrations.AlterField(
            model_name="acuerdo_pago",
            name="codigo_asesor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="acuerdo_pago",
            name="codigo_obligacion",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="acuerdo_pago",
            name="codigo_resultado_gestion",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="acuerdo_pago",
            name="descripcion",
            field=models.CharField(default="sin descripcion", max_length=60),
        ),
        migrations.AlterField(
            model_name="acuerdo_pago",
            name="fecha_gestion",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="acuerdo_pago",
            name="resultado_gestion",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

# Generated by Django 5.0.7 on 2025-01-07 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crm_api", "0008_remove_acuerdo_pago_estado"),
    ]

    operations = [
        migrations.AlterField(
            model_name="acuerdo_pago",
            name="descripcion",
            field=models.CharField(
                blank=True, default="sin descripcion", max_length=60
            ),
        ),
    ]

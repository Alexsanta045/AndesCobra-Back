# Generated by Django 5.0.7 on 2024-12-16 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crm_api", "0002_resultadosgestion_codigo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="resultadosgestion",
            name="descripcion",
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
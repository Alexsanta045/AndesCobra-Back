# Generated by Django 5.0.7 on 2024-12-03 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crm_api", "0003_passwordchangerequest_changed_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="passwordchangerequest",
            name="is_rejected",
            field=models.BooleanField(default=False),
        ),
    ]

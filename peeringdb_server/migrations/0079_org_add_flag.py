# Generated by Django 3.2.7 on 2021-10-28 23:54

import django.core.validators
import django_inet.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("peeringdb_server", "0078_ix_add_error_ixf_import_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="organization",
            name="flagged",
            field=models.BooleanField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="organization",
            name="flagged_date",
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]

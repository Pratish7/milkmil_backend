# Generated by Django 4.2.4 on 2023-08-22 17:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("milkmil", "0032_alter_guests_in_date_alter_guests_in_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="guests",
            name="in_time",
            field=models.TimeField(
                auto_now_add=True,
                default=datetime.datetime(2023, 8, 22, 17, 22, 1, 487071, tzinfo=datetime.timezone.utc),
            ),
            preserve_default=False,
        ),
    ]

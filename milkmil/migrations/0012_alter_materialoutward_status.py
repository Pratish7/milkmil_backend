# Generated by Django 4.2.4 on 2023-08-13 15:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("milkmil", "0011_alter_guests_out_date_alter_guests_out_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="materialoutward",
            name="status",
            field=models.CharField(
                choices=[("QUEUE", "QUEUE"), ("DISPATCHED / COMPLETED", "DISPATCHED / COMPLETED")], default="QUEUE"
            ),
        ),
    ]

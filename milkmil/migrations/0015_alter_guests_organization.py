# Generated by Django 4.2.4 on 2023-08-15 09:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("milkmil", "0014_guests_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="guests",
            name="organization",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

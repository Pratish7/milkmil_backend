# Generated by Django 4.2.4 on 2023-08-16 05:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("milkmil", "0018_barcode"),
    ]

    operations = [
        migrations.AlterField(
            model_name="barcode",
            name="barcode",
            field=models.TextField(),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-16 05:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("milkmil", "0017_materialinward_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="BarCode",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("barcode", models.CharField(max_length=255)),
                ("invoice_num", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
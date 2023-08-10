# Generated by Django 4.2.4 on 2023-08-10 15:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("milkmil", "0007_materialoutward"),
    ]

    operations = [
        migrations.CreateModel(
            name="MaterialInward",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("date", models.DateField(auto_now_add=True)),
                ("invoice_num", models.CharField()),
                ("in_time", models.TimeField(auto_now_add=True)),
                ("out_time", models.TimeField(blank=True, null=True)),
            ],
        ),
    ]

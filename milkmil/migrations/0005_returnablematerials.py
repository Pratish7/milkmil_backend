# Generated by Django 4.2.4 on 2023-08-10 13:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("milkmil", "0004_keys"),
    ]

    operations = [
        migrations.CreateModel(
            name="ReturnableMaterials",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("out_date", models.DateField(auto_now_add=True)),
                ("out_time", models.TimeField(auto_now_add=True)),
                ("gate_pass_num", models.IntegerField()),
                ("in_date", models.DateField(blank=True, null=True)),
                ("in_time", models.TimeField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("YET TO BE RETURNED", "YET TO BE RETURNED"),
                            ("RETURNED / COMPLETED", "RETURNED / COMPLETED"),
                        ]
                    ),
                ),
            ],
        ),
    ]
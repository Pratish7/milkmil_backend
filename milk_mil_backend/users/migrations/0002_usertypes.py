# Generated by Django 4.2.4 on 2023-08-13 16:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserTypes",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "user_type",
                    models.CharField(
                        choices=[
                            ("Data Entry", "Data Entry"),
                            ("QR Code Scan", "QR Code Scan"),
                            ("Photo Clicking", "Photo Clicking"),
                            ("Report Admin", "Report Admin"),
                            ("Material Inward", "Material Inward"),
                            ("Material Outward", "Material Outward"),
                            ("Report View", "Report View"),
                            ("Master Data Admin", "Master Data Admin"),
                            ("Transaction Admin", "Transaction Admin"),
                            ("Visitors Admin", "Visitors Admin"),
                            ("Vehicle Admin", "Vehicle Admin"),
                            ("Status View", "Status View"),
                        ],
                        max_length=255,
                    ),
                ),
            ],
        ),
    ]

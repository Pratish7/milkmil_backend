# Generated by Django 4.2.4 on 2023-08-10 13:51

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("milkmil", "0005_returnablematerials"),
    ]

    operations = [
        migrations.CreateModel(
            name="MasterData",
            fields=[
                ("key", models.CharField(max_length=255, primary_key=True, serialize=False)),
                ("values", django.contrib.postgres.fields.ArrayField(base_field=models.CharField(), size=None)),
            ],
        ),
    ]

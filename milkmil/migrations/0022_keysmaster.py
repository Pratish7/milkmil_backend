# Generated by Django 4.2.4 on 2023-08-20 11:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("milkmil", "0021_alter_keys_key_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="KeysMaster",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("key_type", models.CharField(max_length=255)),
                ("quantity", models.IntegerField()),
                ("bar_code", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
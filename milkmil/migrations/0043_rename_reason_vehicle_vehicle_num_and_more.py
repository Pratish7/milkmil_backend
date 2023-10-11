# Generated by Django 4.2.4 on 2023-09-27 11:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("milkmil", "0042_materialoutward_test_report_num_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="vehicle",
            old_name="reason",
            new_name="vehicle_num",
        ),
        migrations.RemoveField(
            model_name="vehicle",
            name="date",
        ),
        migrations.RemoveField(
            model_name="vehicle",
            name="num_passengers",
        ),
        migrations.RemoveField(
            model_name="vehicle",
            name="out_kms",
        ),
        migrations.RemoveField(
            model_name="vehicle",
            name="type",
        ),
    ]
# Generated by Django 4.2.4 on 2023-08-13 10:23

from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):
    dependencies = [
        ("milkmil", "0008_materialinward"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="keys",
            name="timestamp",
        ),
        migrations.RemoveField(
            model_name="milk",
            name="timestamp",
        ),
        migrations.RemoveField(
            model_name="milk",
            name="type",
        ),
        migrations.RemoveField(
            model_name="vehicle",
            name="timestamp",
        ),
        migrations.AddField(
            model_name="guests",
            name="in_date",
            field=models.DateField(auto_now_add=True, default=timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="guests",
            name="organization",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="guests",
            name="out_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="keys",
            name="person_name",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="milk",
            name="date",
            field=models.DateField(auto_now_add=True, default=timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="milk",
            name="time",
            field=models.TimeField(auto_now_add=True, default=timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="vehicle",
            name="date",
            field=models.DateField(auto_now_add=True, default=timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="guests",
            name="in_time",
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="guests",
            name="out_time",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="guests",
            name="relationship",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="keys",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="keys",
            name="returned_time",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="keys",
            name="taken_time",
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="materialinward",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="materialinward",
            name="invoice_num",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

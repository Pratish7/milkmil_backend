# Generated by Django 4.2.4 on 2023-08-22 15:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("milkmil", "0028_alter_guests_in_time_alter_guests_out_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="guests",
            name="in_time",
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="guests",
            name="out_time",
            field=models.TimeField(default=None, null=True),
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
            name="in_time",
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="materialinward",
            name="out_time",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="materialoutward",
            name="time",
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="milk",
            name="time",
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="returnablematerials",
            name="in_time",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="returnablematerials",
            name="out_time",
            field=models.TimeField(auto_now_add=True),
        ),
    ]

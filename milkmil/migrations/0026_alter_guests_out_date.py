# Generated by Django 4.2.4 on 2023-08-22 14:53

from django.db import migrations
import partial_date.fields


class Migration(migrations.Migration):
    dependencies = [
        ("milkmil", "0025_alter_keys_key_type_alter_keysmaster_key_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="guests",
            name="out_date",
            field=partial_date.fields.PartialDateField(default=None, null=True),
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-04 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0004_colorspantone_colorsraleffect_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='colorsralclassic',
            old_name='html_hex',
            new_name='hex_code',
        ),
    ]

# Generated by Django 2.1.7 on 2022-11-11 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrebolsa', '0005_auto_20221111_0000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='imagen',
            new_name='image',
        ),
    ]

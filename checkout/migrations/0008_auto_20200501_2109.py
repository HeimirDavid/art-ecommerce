# Generated by Django 3.0.5 on 2020-05-01 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_useraddress_address_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraddress',
            old_name='county',
            new_name='country',
        ),
    ]

# Generated by Django 3.0.5 on 2020-05-01 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_useraddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='final_total',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]
# Generated by Django 4.1.5 on 2023-06-03 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userpages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermod',
            name='qr_codes',
        ),
    ]

# Generated by Django 3.2.7 on 2021-09-27 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dungeon', '0012_auto_20210927_0614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zayavka',
            old_name='familiya_clienta',
            new_name='familiya',
        ),
        migrations.RenameField(
            model_name='zayavka',
            old_name='imya_clienta',
            new_name='imya',
        ),
        migrations.RemoveField(
            model_name='zayavka',
            name='extra_info',
        ),
    ]

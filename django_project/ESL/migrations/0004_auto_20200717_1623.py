# Generated by Django 3.0.2 on 2020-07-17 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ESL', '0003_dmarks_tmarks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dmarks',
            old_name='tmarks',
            new_name='dmarks',
        ),
    ]

# Generated by Django 2.2 on 2021-04-19 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='manufecturer',
            new_name='manufacturer',
        ),
    ]

# Generated by Django 3.2.15 on 2022-09-28 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_demo', '0012_auto_20220928_1703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='userid',
            new_name='username',
        ),
    ]

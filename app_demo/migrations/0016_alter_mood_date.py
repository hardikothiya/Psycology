# Generated by Django 3.2.15 on 2022-09-28 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_demo', '0015_auto_20220928_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mood',
            name='date',
            field=models.DateField(auto_now=True, unique=True),
        ),
    ]

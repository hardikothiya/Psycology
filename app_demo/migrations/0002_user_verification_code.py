# Generated by Django 3.2.15 on 2022-08-24 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_demo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verification_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
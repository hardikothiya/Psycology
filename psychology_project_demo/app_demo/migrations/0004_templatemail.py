# Generated by Django 3.2.15 on 2022-08-26 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_demo', '0003_remove_user_password2'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateMail',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('templatetype', models.CharField(max_length=40, unique=True)),
                ('templatevalue', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'db_table': 'demo_mail_template',
            },
        ),
    ]
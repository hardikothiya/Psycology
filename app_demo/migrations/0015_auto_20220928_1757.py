# Generated by Django 3.2.15 on 2022-09-28 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_demo', '0014_auto_20220928_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='userid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_demo.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('mood', models.IntegerField(choices=[(1, 'sorrow'), (2, 'sad'), (3, 'fine'), (4, 'happy'), (5, 'exicted')], default=3, max_length=40)),
                ('date', models.DateField(auto_now=True)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_demo.user')),
            ],
            options={
                'db_table': 'demo_problem',
            },
        ),
    ]

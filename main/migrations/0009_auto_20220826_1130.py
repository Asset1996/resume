# Generated by Django 3.2.15 on 2022-08-26 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20220826_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workexperience',
            name='work_description',
        ),
        migrations.AddField(
            model_name='workexperience',
            name='work_description_en',
            field=models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Brief work description EN'),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='work_description_ru',
            field=models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Brief work description RU'),
        ),
    ]

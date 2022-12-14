# Generated by Django 3.2.15 on 2022-08-26 11:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20220826_1049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workexperience',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='position',
        ),
        migrations.AddField(
            model_name='workexperience',
            name='company_name_en',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Company name EN'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workexperience',
            name='company_name_ru',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Company name RU'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workexperience',
            name='position_en',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Position of the user EN'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workexperience',
            name='position_ru',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Position of the user RU'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.15 on 2022-08-26 06:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20220826_0614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='speciality',
        ),
        migrations.AddField(
            model_name='education',
            name='speciality_en',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Specialty EN'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='education',
            name='speciality_ru',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Specialty RU'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='education',
            name='institution_name_en',
            field=models.CharField(max_length=50, verbose_name='Institution name EN'),
        ),
        migrations.AlterField(
            model_name='education',
            name='institution_name_ru',
            field=models.CharField(max_length=50, verbose_name='Institution name RU'),
        ),
    ]

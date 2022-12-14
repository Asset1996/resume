# Generated by Django 3.2.15 on 2022-08-26 06:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220825_0720'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='institution_name',
            new_name='institution_name_en',
        ),
        migrations.AddField(
            model_name='education',
            name='institution_name_ru',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Institution name'),
            preserve_default=False,
        ),
    ]

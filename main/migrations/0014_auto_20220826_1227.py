# Generated by Django 3.2.15 on 2022-08-26 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20220826_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Addressr'),
        ),
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Date of birth'),
        ),
        migrations.AddField(
            model_name='user',
            name='degree',
            field=models.CharField(choices=[('ms', 'Masters'), ('bc', 'Bachelors'), ('hs', 'High school'), ('nd', 'No degree')], default='bc', max_length=50, verbose_name='Users degree'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='experience',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Experience'),
        ),
        migrations.AddField(
            model_name='user',
            name='github',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Github'),
        ),
        migrations.AddField(
            model_name='user',
            name='instagram',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Instagram'),
        ),
        migrations.AddField(
            model_name='user',
            name='linkedin',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='LinkedIn'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Phone number'),
        ),
    ]

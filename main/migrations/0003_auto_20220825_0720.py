# Generated by Django 3.2.15 on 2022-08-25 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220803_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(choices=[('ms', 'Masters'), ('bc', 'Bachelors'), ('hs', 'High school'), ('nd', 'No degree')], max_length=50, verbose_name='Students degree'),
        ),
        migrations.AlterField(
            model_name='education',
            name='type',
            field=models.CharField(choices=[('un', 'University'), ('cl', 'College'), ('cr', 'Certification')], max_length=50, verbose_name='Type of education'),
        ),
    ]
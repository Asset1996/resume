# Generated by Django 3.2.14 on 2022-08-03 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='company_name',
            field=models.CharField(max_length=50, verbose_name='Company name'),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User name'),
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=50, verbose_name='Institution name')),
                ('speciality', models.CharField(max_length=50, verbose_name='Specialty of user')),
                ('type', models.CharField(choices=[('un', 'University'), ('cl', 'College')], max_length=50, verbose_name='Type of education')),
                ('degree', models.CharField(choices=[('ms', 'Masters'), ('bc', 'Bachelors'), ('hs', 'High school')], max_length=50, verbose_name='Students degree')),
                ('start_date', models.DateField(verbose_name='The date when the user started')),
                ('end_date', models.DateField(blank=True, default=None, null=True, verbose_name='The date when the user graduated')),
                ('course_description', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Brief study description')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User name')),
            ],
            options={
                'ordering': ['end_date'],
            },
        ),
    ]

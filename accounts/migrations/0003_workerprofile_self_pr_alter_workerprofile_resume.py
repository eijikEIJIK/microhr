# Generated by Django 4.0 on 2021-12-21 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_jobseekerprofile_workerprofile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workerprofile',
            name='self_pr',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='workerprofile',
            name='resume',
            field=models.TextField(default=''),
        ),
    ]
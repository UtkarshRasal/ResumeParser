# Generated by Django 3.1.7 on 2021-04-05 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0003_auto_20210405_0627'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumedata',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='resumedata',
            name='file_path',
            field=models.CharField(max_length=255),
        ),
    ]
# Generated by Django 3.1.7 on 2021-04-05 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumedata',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='skills',
            field=models.TextField(blank=True),
        ),
    ]
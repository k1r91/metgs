# Generated by Django 2.1 on 2018-09-28 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_auto_20180924_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='active',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='good',
            name='active',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]

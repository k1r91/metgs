# Generated by Django 2.1 on 2018-09-24 04:46

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20180924_0440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='test',
        ),
        migrations.AlterField(
            model_name='category',
            name='desc',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]

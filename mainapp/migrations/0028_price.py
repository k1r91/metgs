# Generated by Django 2.1 on 2018-10-02 12:34

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0027_auto_20181002_1038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True, verbose_name='Наименовение')),
                ('desc', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Описание')),
                ('file', models.FileField(blank=True, null=True, upload_to='', verbose_name='Файл')),
            ],
        ),
    ]
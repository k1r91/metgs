# Generated by Django 2.1 on 2018-09-21 06:28

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20180921_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='desc',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='category',
            name='related',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='mainapp.Category', verbose_name='Близкие категории'),
        ),
    ]
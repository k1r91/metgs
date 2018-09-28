# Generated by Django 2.1 on 2018-09-28 11:58

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_auto_20180928_0822'),
    ]

    operations = [
        migrations.AddField(
            model_name='topmenu',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='topmenu',
            name='system',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='good',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='good',
            name='desc',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='good',
            name='image',
            field=models.ImageField(upload_to='good', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='good',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='good',
            name='price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='topmenu',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Наполнение'),
        ),
        migrations.AlterField(
            model_name='topmenu',
            name='name',
            field=models.CharField(max_length=32, verbose_name='Наименовение'),
        ),
        migrations.AlterField(
            model_name='topmenu',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='topmenu',
            name='visible',
            field=models.BooleanField(default=True, verbose_name='Видимость'),
        ),
    ]

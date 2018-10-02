# Generated by Django 2.1 on 2018-10-02 13:41

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0029_auto_20181002_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='desc',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='О компании'),
        ),
        migrations.AlterField(
            model_name='news',
            name='desc',
            field=tinymce.models.HTMLField(verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='contact_text',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Контактный текст'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='email',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='footer_desc',
            field=models.TextField(blank=True, null=True, verbose_name='Описание в футере'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='footer_email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email в футере'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='footer_phone',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Телефон в футере'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='logo',
            field=models.ImageField(upload_to='logo', verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='phone',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='phone_prefix',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Код города'),
        ),
    ]

# Generated by Django 2.1 on 2018-10-11 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0031_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoalbum',
            name='main_page',
            field=models.BooleanField(default=False, verbose_name='На главной странице?'),
        ),
    ]
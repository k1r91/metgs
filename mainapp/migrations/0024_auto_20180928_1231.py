# Generated by Django 2.1 on 2018-09-28 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0023_auto_20180928_1228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topmenu',
            old_name='content',
            new_name='desc',
        ),
    ]
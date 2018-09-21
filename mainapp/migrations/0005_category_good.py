# Generated by Django 2.1 on 2018-09-21 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20180917_0945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='category')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='good')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('sub_desc', models.TextField(blank=True, null=True)),
            ],
        ),
    ]

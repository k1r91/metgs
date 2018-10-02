# Generated by Django 2.1 on 2018-10-02 13:15

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0028_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Наименовение')),
                ('desc', tinymce.models.HTMLField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='price',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='price', verbose_name='Файл'),
        ),
    ]
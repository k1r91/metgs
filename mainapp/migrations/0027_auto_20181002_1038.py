# Generated by Django 2.1.1 on 2018-10-02 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0026_auto_20181001_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoalbum',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Наименовение'),
        ),
        migrations.AlterField(
            model_name='photoalbum',
            name='visible',
            field=models.BooleanField(default=True, verbose_name='Видимость'),
        ),
        migrations.AlterField(
            model_name='photoimage',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.PhotoAlbum', verbose_name='Альбом'),
        ),
        migrations.AlterField(
            model_name='photoimage',
            name='visible',
            field=models.BooleanField(default=True, verbose_name='Видимость'),
        ),
    ]
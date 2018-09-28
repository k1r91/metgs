from django.db import models
from tinymce.models import HTMLField


# Create your models here.


class TopMenu(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(unique=True)
    visible = models.BooleanField(default=True)
    content = models.TextField(blank=True, null=True)


class Organization(models.Model):
    logo = models.ImageField(upload_to='logo')
    phone = models.CharField(max_length=64, blank=True, null=True)
    phone_prefix = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=256, blank=True, null=True)
    contact_text = models.CharField(max_length=128, blank=True, null=True)
    footer_email = models.EmailField(blank=True, null=True)
    footer_desc = models.TextField(blank=True, null=True)
    footer_phone = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name="Наименование")
    desc = HTMLField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(upload_to='category', blank=True, null=True, verbose_name="Изображение")
    related = models.ManyToManyField('self', blank=True, null=True, verbose_name="Сопутствующие категории")
    is_active = models.BooleanField(blank=True, default=True, verbose_name='Активна')

    def __str__(self):
        return self.name


class Good(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='good')
    name = models.CharField(max_length=128, unique=True)
    price = models.IntegerField(blank=True, null=True)
    desc = HTMLField(blank=True, null=True)
    sub_desc = models.TextField(blank=True, null=True)
    related = models.ForeignKey('self', blank=True, null=True, on_delete=models.PROTECT)
    is_active = models.BooleanField(blank=True, default=True, verbose_name='Активен')

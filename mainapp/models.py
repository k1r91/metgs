from django.db import models
from tinymce.models import HTMLField


# Create your models here.


class TopMenu(models.Model):
    name = models.CharField(max_length=32, verbose_name="Наименовение")
    slug = models.SlugField(unique=True, verbose_name="Ссылка")
    visible = models.BooleanField(default=True, verbose_name="Видимость")
    desc = HTMLField(blank=True, null=True, verbose_name="Наполнение")
    image = models.ImageField(blank=True, null=True, verbose_name="Изображение")
    system = models.BooleanField(default=False, verbose_name="Системное")


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
    related = models.ManyToManyField('self', blank=True, verbose_name="Сопутствующие категории")
    is_active = models.BooleanField(blank=True, default=True, verbose_name='Активна')

    def __str__(self):
        return self.name


class Good(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name="Наименование")
    price = models.IntegerField(blank=True, null=True, default=0, verbose_name="Цена")
    image = models.ImageField(upload_to='good', blank=True, null=True, verbose_name="Изображение")
    desc = HTMLField(blank=True, null=True, verbose_name="Описание")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Категория")
    related = models.ManyToManyField('self', blank=True, verbose_name="Сопутствующие товары")
    is_active = models.BooleanField(blank=True, default=True, verbose_name="Активен")
    rating = models.IntegerField(blank=True, default=0, null=True, verbose_name="Рейтинг")

    def __str__(self):
        return self.name
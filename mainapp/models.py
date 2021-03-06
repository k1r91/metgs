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
    logo = models.ImageField(upload_to='logo', verbose_name="Логотип")
    desc = HTMLField(verbose_name="О компании", blank=True, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True, verbose_name="Телефон")
    phone_prefix = models.CharField(max_length=10, blank=True, null=True, verbose_name="Код города")
    email = models.CharField(max_length=256, blank=True, null=True, verbose_name="Электронная почта")
    contact_text = models.CharField(max_length=128, blank=True, null=True, verbose_name="Контактный текст")
    footer_email = models.EmailField(blank=True, null=True, verbose_name="Email в футере")
    footer_desc = models.TextField(blank=True, null=True, verbose_name="Описание в футере")
    footer_phone = models.CharField(max_length=64, blank=True, null=True, verbose_name="Телефон в футере")
    name = models.CharField(max_length=64, blank=True, null=True, verbose_name="Наименование")
    main_page_desc = HTMLField(blank=True, null=True, verbose_name="Текст внизу на главной странице")


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


class PhotoAlbum(models.Model):
    name = models.CharField(max_length=128, verbose_name="Наименовение")
    desc = HTMLField(blank=True, null=True, verbose_name="Описание")
    visible = models.BooleanField(default=True, verbose_name="Видимость")
    main_page = models.BooleanField(default=False, verbose_name="На главной странице?")


class PhotoImage(models.Model):
    album = models.ForeignKey(PhotoAlbum, verbose_name="Альбом", on_delete=models.CASCADE,  blank=True, null=True)
    image = models.ImageField(verbose_name="Изображение", upload_to='album')
    desc = HTMLField(blank=True, null=True, verbose_name="Описание")
    name = models.CharField(max_length=128, verbose_name="Наименовение", blank=True, null=True)
    visible = models.BooleanField(default=True, verbose_name="Видимость")


class Price(models.Model):
    name = models.CharField(max_length=128, verbose_name="Наименовение", blank=True, null=True)
    desc = HTMLField(blank=True, null=True, verbose_name="Описание")
    file = models.FileField(verbose_name="Файл", blank=True, null=True, upload_to='price')


class News(models.Model):
    name = models.CharField(max_length=256, verbose_name="Наименовение")
    desc = HTMLField(verbose_name="Содержание")
    date = models.DateTimeField(auto_now_add=True, blank=True)


class Contact(models.Model):
    name = models.CharField(max_length=256, verbose_name="Наименовение")
    desc = HTMLField(blank=True, null=True, verbose_name="Описание")
    map = models.CharField(max_length=256, verbose_name="Ссылка на карту", blank=True, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True, verbose_name="Телефон")
    address = models.TextField(verbose_name="Адрес", blank=True, null=True)
    position = models.CharField(max_length=64, verbose_name="Должность", blank=True, null=True)


class Comment(models.Model):
    name = models.CharField(max_length=256, verbose_name="Ваше имя*")
    contacts = models.CharField(max_length=256, verbose_name="Контакты")
    



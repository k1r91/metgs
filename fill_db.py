import os
import shutil
import django
from django.core.files.images import ImageFile
from django.core.exceptions import ObjectDoesNotExist
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "metgs.settings")
django.setup()
import db_data
from mainapp.models import *


def fill_top_menu():
    TopMenu.objects.all().delete()
    data = db_data.top_menu()
    for item in data:
        try:
            image = ImageFile(open(item.pop('image'), 'rb'))
            model = TopMenu(**item)
            model.image = image
        except KeyError:
            model = TopMenu(**item)
        model.save()
    print('Top menu created.')


def fill_organization():
    Organization.objects.all().delete()
    data = db_data.organization()
    logo = ImageFile(open(data.pop('logo'), 'rb'))
    org = Organization(**data)
    org.logo = logo
    org.save()

    print('Organization created.')


def fill_categories():
    Category.objects.all().delete()
    data = db_data.category()
    for item in data:
        try:
            image = ImageFile(open(item.pop('image'), 'rb'))
            cat = Category(**item)
            cat.image = image
        except KeyError:
            cat = Category(**item)
        finally:
            cat.save()
    print('Categories created.')


def fill_good():
    Good.objects.all().delete()
    data = db_data.good()
    for item in data:
        try:
            category = Category.objects.get(name=item.pop('category_name'))
        except (ObjectDoesNotExist, KeyError):
            category = None
        try:
            image = ImageFile(open(item.pop('image'), 'rb'))
            good = Good(**item)
            good.category = category
            good.image = image
        except KeyError:
            good = Good(**item)
        finally:
            good.save()
    print('Goods created.')


def fill_album():
    PhotoAlbum.objects.all().delete()
    data = db_data.album()
    for item in data:
        album = PhotoAlbum(**item)
        album.save()
    print('Albums created')


def fill_photo():
    PhotoImage.objects.all().delete()
    data = db_data.photo()
    for item in data:
        album = PhotoAlbum.objects.get(name=item["album"])
        image = ImageFile(open(item["image"], 'rb'))
        obj = PhotoImage(album=album, image=image)
        obj.save()
    print('Photos created.')


def fill_news():
    PhotoAlbum.objects.all().delete()
    data = db_data.news()
    for item in data:
        news = News(**item)
        news.save()
    print('News created.')


def fill_contact():
    Contact.objects.all().delete()
    data = db_data.contact()
    for item in data:
        obj = Contact(**item)
        obj.save()
    print('Contacts created.')


if __name__ == '__main__':
    if os.path.exists('media'):
        shutil.rmtree('media')
    fill_top_menu()
    fill_organization()
    fill_categories()
    fill_good()
    fill_album()
    fill_photo()
    fill_news()
    fill_contact()
    pass
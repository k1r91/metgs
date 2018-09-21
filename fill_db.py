import os
import django
from django.core.files.images import ImageFile
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "metgs.settings")
django.setup()
import db_data
from mainapp.models import *


def fill_top_menu():
    TopMenu.objects.all().delete()
    data = db_data.top_menu()
    for item in data:
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


if __name__ == '__main__':
    fill_top_menu()
    fill_organization()
    fill_categories()
    pass
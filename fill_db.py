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


if __name__ == '__main__':
    fill_top_menu()
    fill_organization()
import os
import django
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


if __name__ == '__main__':
    fill_top_menu()
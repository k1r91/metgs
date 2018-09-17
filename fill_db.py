import os
import django
from django.core.files.images import ImageFile
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
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


def test_send_email():
    mail_subject = 'Активация вашего аккаунта на metgs.ru'
    message = render_to_string('acc_active_email.html', {
        'user': 'asd',
        'domain': 'metgs.ru',
        'uid': 'testuid',
        'token': 'testtoken',
    })
    to_email = 'cherkasov.kirill-1@yandex.ru'
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()

if __name__ == '__main__':
    # fill_top_menu()
    # fill_organization()
    # test_send_email()
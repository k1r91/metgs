import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "metgs.settings")
django.setup()
from django.core.files.images import ImageFile
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.contrib.sites.shortcuts import get_current_site
from django.http import Http404, HttpResponse
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from mainapp.models import *
from mainapp.forms import SignUpForm
from mainapp.get_token import account_activation_token
import db_data
from mainapp.models import *
# user = User.objects.get(pk=3)
# uid1 = urlsafe_base64_encode(force_bytes(user.pk))
# print(uid1)
# print(type(uid1))
uid2 = force_text(urlsafe_base64_decode('MTA'.encode()))
print(uid2)

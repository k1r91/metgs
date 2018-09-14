from django.shortcuts import render
from mainapp.models import *
# Create your views here.


def index(request):
    menu_list = TopMenu.objects.all()
    organization = Organization.objects.all()[0]
    return render(request, 'index.html', {'menu_list': menu_list, 'organization': organization})
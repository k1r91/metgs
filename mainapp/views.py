from django.shortcuts import render
from mainapp.models import Category, TopMenu, Organization

# Create your views here.

def get_common_context():
    categories = Category.objects.all()
    menu_list = TopMenu.objects.all()
    organization = Organization.objects.all()[0]
    return {'organization': organization, 'menu_list': menu_list, 'categories': categories}


def index(request):
    context = get_common_context()
    return render(request, 'index.html', context)
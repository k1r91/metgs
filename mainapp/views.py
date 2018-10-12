import random
from django.shortcuts import render
from mainapp.models import *


# Create your views here.


def get_common_context():
    categories = Category.objects.all()
    menu_list = TopMenu.objects.all()
    organization = Organization.objects.all()[0]
    news = News.objects.all().order_by('date')
    if news:
        news = news[:1][0]
    album = random.choice(PhotoAlbum.objects.all())
    photo = random.choice(PhotoImage.objects.filter(album=album))
    return {'organization': organization, 'menu_list': menu_list, 'categories': categories, 'news': news,
            'random_photo': photo}


def index(request):
    context = get_common_context()
    show_categories = Category.objects.all()[:10]
    query_album = PhotoAlbum.objects.filter(main_page=True)
    if query_album:
        album = query_album[0]
    context['album'] = album
    context['show_categories'] = show_categories
    return render(request, 'index.html', context)


def news(request):
    context = get_common_context()
    context['page'] = 'news'
    return render(request, 'news.html', context)


def catalogue(request):
    context = get_common_context()
    context['page'] = 'catalogue'
    return render(request, 'catalogue.html', context)


def price(request):
    context = get_common_context()
    context['page'] = 'price'
    return render(request, 'price.html', context)


def gallery(request):
    context = get_common_context()
    context['page'] = 'gallery'
    return render(request, 'gallery.html', context)


def about(request):
    context = get_common_context()
    context['page'] = 'about'
    return render(request, 'about.html', context)


def technocad(request):
    context = get_common_context()
    context['page'] = 'technocad'
    return render(request, 'technocad.html', context)


def contact(request):
    context = get_common_context()
    context['page'] = 'contact'
    return render(request, 'contact.html', context)

def default(request, default):
    print(default)
    context = get_common_context()
    context['page'] = 'default'
    return render(request, 'default.html', context)

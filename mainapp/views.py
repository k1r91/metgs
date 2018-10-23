import random
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from mainapp.models import *
from mainapp.classes import BreadCrumb


# Create your views here.

def get_common_context():
    categories = Category.objects.all()
    menu_list = TopMenu.objects.all()
    breadcrumbs = [
        BreadCrumb('Главная', '/')
    ]
    organization = Organization.objects.all()[0]
    news = News.objects.all().order_by('date')
    if news:
        news = news[:1][0]
    album = random.choice(PhotoAlbum.objects.all())
    photo = random.choice(PhotoImage.objects.filter(album=album))
    return {'organization': organization, 'menu_list': menu_list, 'categories': categories, 'news': news,
            'random_photo': photo, 'breadcrumbs': breadcrumbs}


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
    context['breadcrumbs'].append(BreadCrumb('Новости', 'news'))
    objects = News.objects.all()
    paginator = Paginator(objects, 10)
    page = request.GET.get('page')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)
    context['objects'] = objects
    return render(request, 'news.html', context)


def news_detail(request, _id):
    context = get_common_context()
    obj = get_object_or_404(News, id=_id)
    context['breadcrumbs'].append(BreadCrumb('Новости', 'news'))
    context['breadcrumbs'].append(BreadCrumb(obj.name, obj.id))
    context['obj'] = obj
    return render(request, 'news_detail.html', context)


def catalogue(request):
    context = get_common_context()
    context['breadcrumbs'].append(BreadCrumb('Каталог', 'catalogue'))
    context['page'] = 'catalogue'
    return render(request, 'catalogue.html', context)


def price(request):
    context = get_common_context()
    context['breadcrumbs'].append(BreadCrumb('Прайс товаров', 'price'))
    context['page'] = 'price'
    return render(request, 'price.html', context)


def gallery(request):
    context = get_common_context()
    context['breadcrumbs'].append(BreadCrumb('Фотогалерея', 'gallery'))
    context['page'] = 'gallery'
    return render(request, 'gallery.html', context)


def about(request):
    context = get_common_context()
    context['breadcrumbs'].append(BreadCrumb('О компании', 'about'))
    context['page'] = 'about'
    return render(request, 'about.html', context)


def contact(request):
    context = get_common_context()
    context['breadcrumbs'].append(BreadCrumb('Контакты', 'contact'))
    contacts = Contact.objects.all()
    places = []
    peoples = []
    for item in contacts:
        if item.map:
            places.append(item)
        if item.position:
            peoples.append(item)
    context['page'] = 'contact'
    context['places'] = places
    context['peoples'] = peoples
    return render(request, 'contact.html', context)


def default(request, default):
    context = get_common_context()
    menu = get_object_or_404(TopMenu, slug=default)
    context['page'] = default
    context['breadcrumbs'].append(BreadCrumb(menu.name, menu.slug))
    return render(request, 'default.html', context)


def feedback(request):
    if request.method == 'POST':
        context = get_common_context()

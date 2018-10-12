from django.shortcuts import render
from mainapp.models import *

# Create your views here.


def get_common_context():
    categories = Category.objects.all()
    menu_list = TopMenu.objects.all()
    organization = Organization.objects.all()[0]
    return {'organization': organization, 'menu_list': menu_list, 'categories': categories}


def index(request):
    context = get_common_context()
    show_categories = Category.objects.all()[:10]
    news = News.objects.all().order_by('date')
    if news:
        news = news[:1][0]
        print(news.name)
    context['news'] = news
    query_album = PhotoAlbum.objects.filter(main_page=True)
    if query_album:
        album = query_album[0]
    context['album'] = album
    context['show_categories'] = show_categories
    return render(request, 'index.html', context)
"""metgs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from AdminApp.views import *
from mainapp.views import *
from UserManagementApp.views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', index),
    path('news/', news),
    path('catalogue/', catalogue),
    path('price/', price),
    path('gallery/', gallery),
    path('about/', about),
    path('technocad/', technocad),
    path('contact/', contact),
    path('<default>/', default),
    path('user/', include('UserManagementApp.urls')),
    path('admin/', include('AdminApp.urls')),
    path('tinymce/', include('tinymce.urls')),
    re_path(r'^tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

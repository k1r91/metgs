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
    path('login/', login),
    path('logout/', logout),
    path('signup/', signup),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('admin/', admin),
    path('admin/get_user_form/<id>/', get_user_form),
    path('admin/user/add/', add_user),
    path('get_category/<id>/', get_category),
    path('admin/get_user/<id>/', get_user),
    path('admin/delete_user/', delete_user),
    path('admin/category/', admin_category),
    path('admin/category/delete/<_id>/', delete_category),
    path('admin/category/add/', add_category),
    path('admin/category/edit/<_id>/', edit_category),
    path('tinymce/', include('tinymce.urls')),
    re_path(r'^tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path

from AdminApp.views import *

urlpatterns = [
    path('', admin),
    path('get_user_form/<id>/', get_user_form),
    path('user/add/', add_user),
    path('get_category/<id>/', get_category),
    path('get_user/<id>/', get_user),
    path('delete_user/', delete_user),
    path('category/', admin_category),
    path('category/delete/<_id>/', delete_category),
    path('category/add/', add_category),
    path('category/edit/<_id>/', edit_category),
]

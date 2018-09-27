from django.urls import path
from UserManagementApp.views import *

urlpatterns = [
    path('login/', login),
    path('logout/', logout),
    path('signup/', signup),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
]

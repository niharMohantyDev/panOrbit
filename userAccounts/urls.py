from django.urls import path
from .views import *

urlpatterns = [
    path('', signup, name='signup'),
    path('login/', login, name='login'),
    path('search/', search, name='search'),
    path('autosuggest/', autosuggest, name='autosuggest'),
    path('oldUserLogin/', oldUserLogin, name='oldUserLogin'),
    path('logout/', logout_view, name='logout'),
]

from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', view_menu, name='menu'),
    path('companies/', view_menu2, name='com'),
    path('add_company/', view_menu3, name='com'),
    path('types/', view_menu4, name='com'),
    path('add_type/', view_menu5, name='com'),
    path('edit_type/<slug:slug>', view_menu6, name='com'),
    path('delete_type/<slug:slug>', view_menu7, name='com'),
    path('edit_company/<slug:slug>', view_menu8, name='com'),
    path('delete_company/<slug:slug>', view_menu9, name='com'),
    path('add_company/', view_menu10, name='com'),
    path('workers/', view_menu11, name='com'),
    path('add_worker/', view_menu12, name='com'),
    path('edit_worker/<slug:slug>', view_menu13, name='com'),
    path('editions', view_menu14, name='com'),
    path('add_edition', view_menu15, name='com'),
    path('edit_edition/<slug:slug>', view_menu16),
    path('delete_edition/<slug:slug>', view_menu17),
    path('registration', view_menu18),
    path('auth', view_menu19),
]

from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', view_menu, name='menu'),
    path('companes', get_companies, name='companes'),
    path('workers', get_workers, name='workers'),
    path('all_types', get_types, name='types'),
    path('editions', get_editions, name='editions'),
    path('delete_type/<slug:type_slug>/', delete_type, name='delete_type'),
    path('edit_type/<slug:type_slug>/', edit_type, name='edit_type'),
    path('add_type/', add_type, name='add_type'),
    path('add_company/', add_company, name='add_company'),
    path('add_worker/', add_worker, name='add_worker'),
    path('add_edition/', add_edition, name='add_edition'),
    path('delete_edition/<slug:edition_slug>', delete_edition, name='delete_edition'),
    path('edit_edition/<slug:edition_slug>', edit_edition, name='edit_edition'),
    path('delete_worker/<slug:worker_slug>', delete_worker, name='delete_worker'),
    path('edit_worker/<slug:worker_slug>', edit_worker, name='edit_worker'),
    path('delete_company/<slug:company_slug>', delete_company, name='delete_company'),
    path('edit_company/<slug:company_slug>', edit_company, name='edit_company'),
]
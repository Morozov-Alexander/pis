from django.urls import path
from .views import *

urlpatterns = [
    path('', menu, name='menu'),
    path('companes', viewComanes.as_view(), name='companes'),
    path('edit_company/<slug:company_slug>', EditCompany.as_view(), name='edit_company'),
    path('delete_company/<slug:company_slug>', deleteCompany, name='delete_company'),
    path('add_company', AddCompany.as_view(), name='add_company'),
    path('workers', viewWorkers.as_view(), name='workers'),
    path('add_worker', AddWorker.as_view(), name='add_worker'),
    path('edit_worker/<slug:worker_slug>', UpdateWorker.as_view(), name='edit_worker'),
    path('add_worker/<slug:worker_slug>', delete_worker, name='delete_worker'),
]

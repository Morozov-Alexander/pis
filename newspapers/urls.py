from django.urls import path
from .views import *

urlpatterns = [
    path('', menu, name='menu'),
    path('/companes', viewComanes.as_view(), name='companes'),
    path('/edit_company/<slug:company_slug>', EditCompany.as_view(), name='edit_company'),
    path('/delete_company/<slug:company_slug>', deleteCompany, name='delete_company'),
    path('/add_company', AddCompany.as_view(), name='add_company'),
]

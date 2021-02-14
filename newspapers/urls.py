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
    path('all_types', viewTypes.as_view(), name='types'),
    path('add_type', addType.as_view(), name='add_type'),
    path('edit_type/<slug:type_slug>', UpdateType.as_view(), name='edit_type'),
    path('delete_type/<slug:type_slug>', delete_type, name='delete_type'),
    path('editions', viewEditions.as_view(), name='editions'),
    path('add_editions', addEdition.as_view(), name='add_editions'),
    path('edit_editions/<slug:edition_slug>', UpdateEdition.as_view(), name='edit_editions'),
    path('delete_editions/<slug:edition_slug>', delete_edition, name='delete_editions'),
    # --------------------------------------------------------------------
    path('companies_json', CompanyJsonView.as_view(), name='companes_json'),
    path('workers_json', WorkersJsonView.as_view(), name='workers_json'),
    path('companies_json/<slug:company_slug>', ConcreteJsonCompany.as_view(), name='concrete_companes_json'),
    path('workers_json/<slug:worker_slug>', viewJsonConcreteWorker.as_view(), name='concrete_workers_json'),
    path('all_types_json', viewJsonTypes.as_view(), name='types_json'),
    # TODO:Вывод всех изданий для типа
    path('all_types_json/<slug:type_slug>', viewConcreteType.as_view(), name='concrete_types_json'),
    path('editions_json', viewAllEditions.as_view(), name='editions_json'),
    path('editions_json/<slug:edition_slug>', viewConcreteEdition.as_view(), name='concrete_editions_json'),
]

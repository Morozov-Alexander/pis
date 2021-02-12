from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import *
from .forms import *
import logging

logging.basicConfig(level=logging.INFO, filename='my_log.log')


def menu(request):
    return render(request, 'menu.html')


class viewComanes(ListView):
    model = Company
    template_name = 'all_companes.html'
    context_object_name = 'companes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        logging.info('Show info about companes')
        context['name'] = 'Компании'
        return context


class EditCompany(UpdateView):
    model = Company
    success_url = reverse_lazy('companes')
    template_name = 'edit_company.html'
    form_class = EditCompany
    slug_url_kwarg = 'company_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        logging.info('Edit info about company')
        context['name'] = 'Редактирование компании'
        return context


def deleteCompany(request, company_slug):
    logging.info(f'Delete company {Company.objects.get(slug=company_slug)}')
    Company.objects.get(slug=company_slug).delete()
    return redirect('companes')


class AddCompany(CreateView):
    success_url = reverse_lazy('companes')
    template_name = 'edit_company.html'
    form_class = CreateComapany

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        logging.info('Create company')
        context['name'] = 'Добавление компании'
        return context


class viewWorkers(ListView):
    model = Worker
    template_name = 'all_workers.html'
    context_object_name = 'workers'


class AddWorker(CreateView):
    form_class = CreateWorker
    success_url = reverse_lazy('workers')
    template_name = 'edit_company.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logging.info('Create new worker')
        context['name'] = 'Добавление работника'
        return context


class UpdateWorker(UpdateView):
    model = Worker
    form_class = CreateWorker
    success_url = reverse_lazy('workers')
    template_name = 'edit_company.html'
    slug_url_kwarg = 'worker_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logging.info('Update info about worker')
        context['name'] = 'Редактирование работника'
        return context


def delete_worker(request, worker_slug):
    logging.info(f'Delte worker {Worker.objects.get(slug=worker_slug)}')
    Worker.objects.get(slug=worker_slug).delete()
    return redirect('workers')


class viewTypes(ListView):
    model = TypeOfEdition
    template_name = 'all_types.html'
    context_object_name = 'types'


class addType(CreateView):
    form_class = AddType
    model = TypeOfEdition
    success_url = reverse_lazy('types')
    template_name = 'edit_company.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logging.info('Create new type')
        context['name'] = 'Добавление типа'
        return context


class UpdateType(UpdateView):
    model = TypeOfEdition
    form_class = AddType
    template_name = 'edit_company.html'
    success_url = reverse_lazy('types')
    slug_url_kwarg = 'type_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logging.info('Update info about type')
        context['name'] = 'Редатирование типа'
        return context


def delete_type(request, type_slug):
    logging.info(f'Delete type {TypeOfEdition.objects.get(slug=type_slug)}')
    TypeOfEdition.objects.get(slug=type_slug).delete()
    return redirect('types')


class viewEditions(ListView):
    model = Edition
    context_object_name = 'editions'
    template_name = 'all_editions.html'


class addEdition(CreateView):
    model = Edition
    form_class = AddEdition
    success_url = reverse_lazy('editions')
    template_name = 'edit_company.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logging.info('Create new edition')
        context['name'] = 'Добавление издания'
        return context


class UpdateEdition(UpdateView):
    model = Edition
    form_class = AddEdition
    template_name = 'edit_company.html'
    success_url = reverse_lazy('editions')
    slug_url_kwarg = 'edition_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logging.info('Update info about edition')
        context['name'] = 'Редатирование издания'
        return context


def delete_edition(request, edition_slug):
    logging.info(f'Delete edition {Edition.objects.get(slug=edition_slug)}')
    Edition.objects.get(slug=edition_slug).delete()
    return redirect('editions')

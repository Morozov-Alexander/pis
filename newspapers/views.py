from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import *
from .forms import *
import logging
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView

logging.basicConfig(level=logging.INFO, filename='log.log')


def menu(request):
    return render(request, 'menu.html')


class viewComanes(ListView):
    model = Company
    template_name = 'all_companes.html'
    context_object_name = 'companes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        logging.info('Show info about companies')
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


# JSON ------------------------------


class CompanyJsonView(APIView):

    def get(self, request):
        companies = Company.objects.all()
        serializer = serializerCompany(companies, many=True)
        return Response(serializer.data)

    def post(self, request):
        temp = serializerCompany(data=request.data)
        if temp.is_valid():
            temp.save()
            return Response(status=201)
        else:
            return Response(status=404)


class ConcreteJsonCompany(APIView):
    def get(self, request, company_slug):
        try:
            company = Company.objects.get(slug=company_slug)
        except:
            return Response(status=404)
        serializer = serializуConcreteCompany(company)
        return Response(serializer.data)

    def put(self, request, company_slug):
        try:
            company = Company.objects.get(slug=company_slug)
        except:
            return Response(status=404)
        company.name = request.data['name']
        company.slug = request.data['slug']
        company.save()
        return Response(status=201)

    def delete(self, request, company_slug):
        try:
            Company.objects.get(slug=company_slug).delete()
        except:
            return Response(status=404)
        return Response(status=200)


class WorkersJsonView(APIView):
    def get(self, request):
        workers = Worker.objects.all()
        serialize = serializeWorkers(workers, many=True)
        return Response(serialize.data)

    def post(self, request):
        """Обработка создания нового работника post-запрос"""
        temp = serializeWorkers(data=request.data)
        if temp.is_valid():
            temp.save()
            return Response(status=201)
        else:
            return Response(status=404)


class viewJsonConcreteWorker(APIView):
    def get(self, request, worker_slug):
        try:
            worker = Worker.objects.get(slug=worker_slug)
        except:
            return Response(status=404)
        data = serializeConcreteWorker(worker)
        return Response(data.data)

    def put(self, request, worker_slug):
        try:
            worker = Worker.objects.get(slug=worker_slug)
        except:
            return Response(status=404)
        worker.first_name = request.data['first_name']
        worker.second_name = request.data['second_name']
        worker.slug = request.data['slug']
        try:
            worker.company = Company.objects.get(id=request.data['company'])
        except:
            return Response(status=404)
        worker.save()
        return Response(status=201)

    def delete(self, request, company_slug):
        try:
            Worker.objects.get(slug=company_slug).delete()
        except:
            return Response(status=404)
        return Response(status=200)


class viewJsonTypes(APIView):
    def get(self, request):
        types = TypeOfEdition.objects.all()
        serialize = serializeTypes(types, many=True)
        return Response(serialize.data)

    def post(self, request):
        temp = serializeTypes(data=request.data)
        if temp.is_valid():
            temp.save()
        return Response(status=201)


class viewConcreteType(APIView):
    def get(self, request, type_slug):
        try:
            type = TypeOfEdition.objects.get(slug=type_slug)
        except:
            return Response(status=404)
        temp = serializeConcreteType(type)
        return Response(temp.data)

    def put(self, request, type_slug):
        try:
            type = TypeOfEdition.objects.get(slug=type_slug)
        except:
            return Response(status=404)
        type.type = request.data['type']
        type.slug = request.data['slug']
        type.save()
        return Response(status=201)

    def delete(self, request, company_slug):
        try:
            TypeOfEdition.objects.get(slug=company_slug).delete()
        except:
            return Response(status=404)
        return Response(status=200)


class viewAllEditions(APIView):
    def get(self, request):
        editions = Edition.objects.all()
        serialize = serializeEditions(editions, many=True)
        return Response(serialize.data)

    def post(self, request):
        respons = serializeEditions(data=request.data)
        if respons.is_valid():
            respons.save()
        return Response(status=201)


class viewConcreteEdition(APIView):
    def get(self, request, edition_slug):
        ediotion = Edition.objects.get(slug=edition_slug)
        temp = serializeConcreteEdition(ediotion)
        return Response(temp.data)
    # TODO:add_put

from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import *
from .forms import *


def menu(request):
    return render(request, 'menu.html')


class viewComanes(ListView):
    model = Company
    template_name = 'all_companes.html'
    context_object_name = 'companes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
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

        context['name'] = 'Редактирование компании'
        return context


def deleteCompany(request, company_slug):
    Company.objects.get(slug=company_slug).delete()
    return redirect('companes')


class AddCompany(CreateView):
    success_url = reverse_lazy('companes')
    template_name = 'edit_company.html'
    form_class = CreateComapany

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Добавление компании'
        return context

from typing import Any

import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def view_menu(request):
    return render(request, 'index.html')


def view_menu2(request):
    return render(request, 'index.html')


def view_menu3(request):
    return render(request, 'index.html')


def view_menu4(request):
    return render(request, 'index.html')


def view_menu5(request):
    return render(request, 'index.html')


def view_menu7(request, slug):
    return render(request, 'index.html')


def view_menu6(request, slug):
    return render(request, 'index.html')


# def get_companies(request):
#     context = {}
#     url = 'http://127.0.0.1:8001/menu/companies_json'
#     context['data'] = requests.get(url).json()
#     return render(request, 'all_companies.html', context)

def get_companies2(request):
    return render(request, 'index.html')


def get_workers(request):
    url = 'http://127.0.0.1:8001/menu/workers_json'
    context: dict[str, Any] = {'data': requests.get(url).json()}
    return render(request, 'all_workers.html', context)


def get_types(request):
    url = 'http://127.0.0.1:8001/menu/all_types_json'
    context = {'data': requests.get(url).json()}
    return render(request, 'all_types.html', context)


def get_editions(request):
    url = 'http://127.0.0.1:8001/menu/editions_json'
    context = {'data': requests.get(url).json()}
    return render(request, 'all_editions.html', context)


def delete_type(request, type_slug):
    url = f'http://127.0.0.1:8001/menu/all_types_json/{type_slug}'
    response = requests.delete(url)
    if response.status_code == 200:
        return redirect('types')
    else:
        return HttpResponse('<h1>Повезло повезло...</h1>')


def add_type(request):
    url = 'http://127.0.0.1:8001/menu/all_types_json'
    if request.method == 'POST':
        result = {'type': request.POST['type'], 'slug': request.POST['slug']}
        response = requests.post(url, result)
        if response.status_code == 201:
            return redirect('types')
        else:
            return HttpResponse('<h1>Повезло повезло...</h1>')
    else:
        return render(request, 'add_type.html')


def edit_type(request, type_slug):
    url = f'http://127.0.0.1:8001/menu/all_types_json/{type_slug}'
    if request.method == 'POST':
        result = {'type': request.POST['type'], 'slug': request.POST['slug']}
        response = requests.put(url, result)
        if response.status_code == 201:
            return redirect('types')
        else:
            return HttpResponse('<h1>Повезло повезло...</h1>')
    else:
        return render(request, 'add_type.html')


def add_company(request):
    url = 'http://127.0.0.1:8001/menu/companies_json'
    if request.method == 'POST':
        result = {'name': request.POST['name'], 'slug': request.POST['slug']}
        response = requests.post(url, result)
        if response.status_code == 201:
            return redirect('companes')
        else:
            return HttpResponse('<h1>Повезло повезло...</h1>')
    else:
        return render(request, 'add_company.html')


def delete_company(request, company_slug):
    url = f'http://127.0.0.1:8001/menu/companies_json/{company_slug}'
    respons = requests.delete(url)
    if respons.status_code == 200:
        return redirect('companes')
    else:
        return HttpResponse('<h1>Повезло повезло...</h1>')


def edit_company(request, company_slug):
    url = f'http://127.0.0.1:8001/menu/companies_json/{company_slug}'
    if request.method == 'POST':
        result = {'name': request.POST['name'], 'slug': request.POST['slug']}
        response = requests.put(url, result)
        if response.status_code == 201:
            return redirect('companes')
        else:
            return HttpResponse('<h1>Повезло повезло...</h1>')
    else:
        return render(request, 'add_company.html')


def add_worker(request):
    url = 'http://127.0.0.1:8001/menu/workers_json2'
    if request.method == 'POST':
        result = {'first_name': request.POST['first_name'], 'second_name': request.POST['second_name'],
                  'slug': request.POST['slug'], 'company': request.POST['company']}
        respons = requests.post(url, result)
        if respons.status_code == 201:
            return redirect('workers')
        else:
            return HttpResponse('<h1>Повезло повезло...</h1>')
    else:
        context = {}
        url = 'http://127.0.0.1:8001/menu/companies_json'
        context['data'] = requests.get(url).json()
        return render(request, 'add_worker.html', context)


def edit_worker(request, worker_slug):
    url = f'http://127.0.0.1:8001/menu/workers_json/{worker_slug}'
    if request.method == 'POST':
        result = {'first_name': request.POST['first_name'], 'second_name': request.POST['second_name'],
                  'slug': request.POST['slug'], 'company': request.POST['company']}
        print(result['company'])
        respons = requests.put(url, result)
        if respons.status_code == 201:
            return redirect('workers')
        else:
            return HttpResponse('<h1>ХУета</h1>')
    else:
        context = {}
        url = 'http://127.0.0.1:8001/menu/companies_json'
        context['data'] = requests.get(url).json()
        return render(request, 'add_worker.html', context)


def delete_worker(request, worker_slug):
    url = f'http://127.0.0.1:8001/menu/workers_json/{worker_slug}'
    respons = requests.delete(url)
    if respons.status_code == 200:
        return redirect('workers')
    else:
        return HttpResponse('<h1>Повезло повезло...</h1>')


def add_edition(request):
    if request.method == 'POST':
        url = 'http://127.0.0.1:8001/menu/editions_json2'
        result = {
            'name_of_the_edition': request.POST['name_of_the_edition'],
            'start_data': request.POST['start_data'],
            'end_data': request.POST['end_data'],
            'slug': request.POST['slug'],
            'worker': request.POST.getlist('worker'),
            'type': request.POST['type']
        }

        respons = requests.post(url, result)
        if respons.status_code == 201:
            return redirect('editions')
        else:
            return HttpResponse('<h1>Повезло повезло...</h1>')
    else:
        url = 'http://127.0.0.1:8001/menu/workers_json'
        context: dict[str, Any] = {'workers': requests.get(url).json()}
        url = 'http://127.0.0.1:8001/menu/all_types_json'
        context['types'] = requests.get(url).json()
        return render(request, 'add_edition.html', context)


def delete_edition(request, edition_slug):
    url = f'http://127.0.0.1:8001/menu/editions_json/{edition_slug}'
    respons = requests.delete(url)
    if respons.status_code == 200:
        return redirect('editions')
    else:
        return HttpResponse('<h1>Повезло повезло...</h1>')


def edit_edition(request, edition_slug):
    if request.method == 'POST':
        url = f'http://127.0.0.1:8001/menu/editions_json/{edition_slug}'
        result = {
            'name_of_the_edition': request.POST['name_of_the_edition'],
            'start_data': request.POST['start_data'],
            'end_data': request.POST['end_data'],
            'slug': request.POST['slug'],
            'worker': list(map(int, request.POST.getlist('worker'))),
            'type': request.POST['type']
        }
        response = requests.put(url, result)
        if response.status_code == 201:
            return redirect('editions')
        else:
            return HttpResponse('<h1>Повезло повезло...</h1>')
    else:
        url = 'http://127.0.0.1:8001/menu/workers_json'
        context: dict[str, Any] = {'workers': requests.get(url).json()}
        url = 'http://127.0.0.1:8001/menu/all_types_json'
        context['types'] = requests.get(url).json()
        return render(request, 'add_edition.html', context)

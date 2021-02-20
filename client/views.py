from typing import Any

import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def view_menu(request):
    return render(request, 'index.html')


def view_menu16(request, slug):
    return render(request, 'index.html')


def view_menu17(request, slug):
    return render(request, 'index.html')


def view_menu11(request):
    return render(request, 'index.html')


def view_menu12(request):
    return render(request, 'index.html')


def view_menu13(request, slug):
    return render(request, 'index.html')


def view_menu2(request):
    return render(request, 'index.html')


def view_menu3(request):
    return render(request, 'index.html')


def view_menu15(request):
    return render(request, 'index.html')


def view_menu14(request):
    return render(request, 'index.html')


def view_menu4(request):
    return render(request, 'index.html')


def view_menu5(request):
    return render(request, 'index.html')


def view_menu7(request, slug):
    return render(request, 'index.html')


def view_menu6(request, slug):
    return render(request, 'index.html')


def view_menu8(request, slug):
    return render(request, 'index.html')


def view_menu9(request, slug):
    return render(request, 'index.html')


def view_menu10(request):
    return render(request, 'index.html')

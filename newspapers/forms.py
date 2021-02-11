from django import forms
from .models import *


class EditCompany(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'slug']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control mr-sm-2', 'placeholder': 'Название компании', 'type': 'text'
                       }),
            'slug': forms.TextInput(
                attrs={'class': 'form-input form-control mr-sm-2', 'placeholder': 'URL', 'type': 'text'})
        }


class CreateComapany(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'slug']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control mr-sm-2', 'placeholder': 'Название компании', 'type': 'text'
                       }),
            'slug': forms.TextInput(
                attrs={'class': 'form-input form-control mr-sm-2', 'placeholder': 'URL', 'type': 'text'})
        }


class CreateWorker(forms.ModelForm):
    class Meta:
        model = Worker
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control mr-sm-2', 'placeholder': 'Имя работника', 'type': 'text'
                       }),
            'second_name': forms.TextInput(
                attrs={'class': 'form-input form-control mr-sm-2', 'placeholder': 'Фамилия работника', 'type': 'text'}),
            'slug': forms.TextInput(
                attrs={'class': 'form-control mr-sm-2', 'placeholder': 'URL', 'type': 'text'
                       }),
        }


class AddType(forms.ModelForm):
    class Meta:
        model = TypeOfEdition
        fields = '__all__'
        widgets = {
            'type': forms.TextInput(
                attrs={'class': 'form-control mr-sm-2', 'placeholder': 'Тип', 'type': 'text'
                       }),
            'slug': forms.TextInput(
                attrs={'class': 'form-input form-control mr-sm-2', 'placeholder': 'URL', 'type': 'text'})
        }


class AddEdition(forms.ModelForm):
    class Meta:
        model = Edition
        fields = '__all__'
        widgets = {
            'name_of_the_edition': forms.TextInput(
                attrs={'class': 'form-control mr-sm-2', 'placeholder': 'Издание', 'type': 'text'
                       }),
            'start_data': forms.TextInput(
                attrs={'class': 'form-input form-control mr-sm-2', 'placeholder': 'Начало подписки', 'type': 'text'}),
            'end_data': forms.TextInput(
                attrs={'class': 'form-control mr-sm-2', 'placeholder': 'Конец Подписки', 'type': 'text'
                       }),
            'slug': forms.TextInput(
                attrs={'class': 'form-input form-control mr-sm-2', 'placeholder': 'URL', 'type': 'text'})
        }

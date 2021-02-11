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

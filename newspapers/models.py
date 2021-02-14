from django.db import models
from slugify import slugify


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название компании')
    slug = models.SlugField(max_length=100, db_index=True, verbose_name='URL')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return f'Company {self.name}'

    class Meta:
        ordering = ['name']
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Worker(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    second_name = models.CharField(max_length=100, verbose_name='Фамилия')
    slug = models.SlugField(max_length=100, db_index=True, verbose_name='URL')
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name='worker')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return f'{self.first_name}'

    class Meta:
        ordering = ['second_name']
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'


class TypeOfEdition(models.Model):
    type = models.CharField(max_length=100, verbose_name='Тип')
    slug = models.SlugField(max_length=100, verbose_name='URL')

    def __str__(self):
        return f'{self.type}'

    class Meta:
        ordering = ['type']
        verbose_name = 'Тип издания'
        verbose_name_plural = 'Типы изданий'


class Edition(models.Model):
    name_of_the_edition = models.CharField(max_length=100, verbose_name='Название газеты')
    start_data = models.DateField(verbose_name='Дата начала подписки')
    end_data = models.DateField(verbose_name='Дата конца подписки')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')
    worker = models.ManyToManyField(Worker, related_name='edition')
    type = models.ForeignKey(TypeOfEdition, on_delete=models.PROTECT, related_name='edition')

    def __str__(self):
        return self.name_of_the_edition

    def __unicode__(self):
        return self.name_of_the_edition

    class Meta:
        ordering = ['name_of_the_edition']
        verbose_name = 'Издание'
        verbose_name_plural = 'Издания'

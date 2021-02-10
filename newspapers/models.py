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

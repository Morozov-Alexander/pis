from rest_framework import serializers
from .models import *


class serializeWorkers(serializers.ModelSerializer):
    # company = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Worker
        fields = '__all__'


class serializerCompany(serializers.ModelSerializer):
    """Сериалайзер для компании"""
    worker = serializeWorkers(many=True)

    class Meta:
        model = Company
        fields = '__all__'


class serializуConcreteCompany(serializers.ModelSerializer):
    """Сериализация конкретной компании"""
    worker = serializeWorkers(many=True)

    class Meta:
        model = Company
        fields = '__all__'


class serializeConcreteWorker(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'


class serializeTypes(serializers.ModelSerializer):
    class Meta:
        model = TypeOfEdition
        fields = '__all__'

from rest_framework import serializers
from .models import *


class serializeEditions(serializers.ModelSerializer):
    class Meta:
        model = Edition
        fields = '__all__'


class serializeWorkers(serializers.ModelSerializer):
    company = serializers.SlugRelatedField(slug_field='name', read_only=True)
    edition = serializeEditions(many=True, read_only=True)

    class Meta:
        model = Worker
        fields = '__all__'


class serializerCompany(serializers.ModelSerializer):
    """Сериалайзер для компании"""
    worker = serializeWorkers(many=True, read_only=True)

    class Meta:
        model = Company
        fields = '__all__'


class serializуConcreteCompany(serializers.ModelSerializer):
    """Сериализация конкретной компании"""

    worker = serializeWorkers(many=True, read_only=True)

    class Meta:
        model = Company
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data['slug'])


class serializeConcreteWorker(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'


class serializeTypes(serializers.ModelSerializer):
    edition = serializeEditions(many=True, read_only=True)

    class Meta:
        model = TypeOfEdition
        fields = '__all__'


class serializeConcreteType(serializers.ModelSerializer):
    class Meta:
        model = TypeOfEdition
        fields = '__all__'


class serializeConcreteEdition(serializers.ModelSerializer):
    class Meta:
        model = Edition
        fields = '__all__'

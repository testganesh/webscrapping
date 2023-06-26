from rest_framework import serializers
from .models import Service, Action, Resource, Condition

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['resourceType', 'arn']

class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = ['conditionKey', 'desc', 'typ']

class ActionSerializer(serializers.ModelSerializer):
    resources = ResourceSerializer(many=True)
    conditionKeys = ConditionSerializer(many=True)

    class Meta:
        model = Action
        fields = ['action', 'access', 'resources', 'conditionKeys', 'desc']

class ServiceSerializer(serializers.ModelSerializer):
    actions = ActionSerializer(many=True)
    resources = ResourceSerializer(many=True)
    conditions = ConditionSerializer(many=True)

    class Meta:
        model = Service
        fields = ['prefix', 'link', 'actions', 'resources', 'conditions']

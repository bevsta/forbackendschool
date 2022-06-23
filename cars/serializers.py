from rest_framework import serializers
from cars.models import Item


class ItemsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('type', 'name', 'id', 'parentId', 'price', 'date', 'children')
        depth = 1

class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


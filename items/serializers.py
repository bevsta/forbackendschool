from rest_framework import serializers
from items.models import Item
from rest_framework_recursive.fields import RecursiveField


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


# Формирует список (дерево) категорий и товаров
class ItemsListSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ('type', 'name', 'id', 'parentId', 'price', 'date', 'children')


# Просмотр, создание и редактирование
class ItemDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    children = RecursiveSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ('type', 'name', 'id', 'parentId', 'price', 'date', 'children', 'user')


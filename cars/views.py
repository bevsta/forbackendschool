from django.shortcuts import render
from rest_framework import generics, filters
from cars.serializers import ItemDetailSerializer, ItemsListSerializer
from cars.models import Item
from cars.permissions import IsOwnerOrReadOnly
# Create your views here.


# Создание записи о Позиции
class ItemCreateView(generics.CreateAPIView):
    serializer_class = ItemDetailSerializer


# Просмотр списка Позиций
class ItemsListView(generics.ListAPIView):
    serializer_class = ItemsListSerializer
    queryset = Item.objects.filter(parentId=None)
    filter_backends = [filters.OrderingFilter]
    #ordering_fields = ['vin', 'brand']
    ordering = ['name']


# Чтоение записи о Позиции
class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemDetailSerializer
    queryset = Item.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
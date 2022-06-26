from django.shortcuts import render
from rest_framework import generics, filters
from items.serializers import ItemDetailSerializer, ItemsListSerializer
from items.models import Item
from items.permissions import IsOwnerOrReadOnly
# Create your views here.


# Создание записи о Позиции
class ItemCreateView(generics.CreateAPIView):
    serializer_class = ItemDetailSerializer


# Просмотр списка Позиций
class ItemsListView(generics.ListAPIView):
    serializer_class = ItemsListSerializer
    queryset = Item.objects.filter(parentId=None)
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['']
    # ordering = ['name']


# Чтоение записи о Позиции
class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemDetailSerializer
    queryset = Item.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )

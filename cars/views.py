from django.shortcuts import render
from rest_framework import generics, filters
from cars.serializers import ItemDetailSerializer, ItemsListSerializer
from cars.models import Item

# Create your views here.


# Создание записи о машине
class ItemCreateView(generics.CreateAPIView):
    serializer_class = ItemDetailSerializer


# Просмотр списка машин
class ItemsListView(generics.ListAPIView):
    serializer_class = ItemsListSerializer
    queryset = Item.objects.all()
    filter_backends = [filters.OrderingFilter]
    #ordering_fields = ['vin', 'brand']
    ordering = ['parentId']


# Чтоение записи о машине
class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemDetailSerializer
    queryset = Item.objects.all()
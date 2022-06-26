from django.urls import path
from items.views import *

urlpatterns = [
    path('imports/', ItemCreateView.as_view()),
    path('all/', ItemsListView.as_view()),
    path('nodes/<str:pk>', ItemDetailView.as_view()),
]

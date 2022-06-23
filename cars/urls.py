from django.urls import path
from . import views
from cars.views import *

urlpatterns = [
    path('imports/', ItemCreateView.as_view()),
    path('all/', ItemsListView.as_view()),
    path('nodes/<int:pk>', ItemDetailView.as_view())
]

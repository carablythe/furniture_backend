#map request URLs to the views created in views.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/furnitures', views.FurnitureList.as_view(), name = 'furniture_list'),
    path('api/furnitures/<int:pk>', views.FurnitureDetail.as_view(), name = 'furniture_detail'),
]

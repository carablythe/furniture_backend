from django.urls import path
from . import views

urlpatterns = [
    path('api/furnitures', views.FurnitureList.as_view(), name='furniture_list'), # api/furnitures will be routed to the FurnitureList view for handling
    path('api/furnitures/<int:pk>', views.FurnitureDetail.as_view(), name='funiture_detail'), # api/furnitures/id will be routed to the FurnitureDetail view for handling


    path('api/carts', views.CartList.as_view(), name='cart_list'),
    path('api/carts/<int:pk>', views.CartDetail.as_view(), name='cart_detail'),

    path('api/reviews', views.ReviewList.as_view(), name='review_list'),
    path('api/reviews/<int:pk>', views.ReviewDetail.as_view(), name='review_detail'),


]

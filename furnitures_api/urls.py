#map request URLs to the views created in views.py
from django.urls import path
from . import views


urlpatterns = [

   path('api/users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/users/register', views.registerUser, name = 'register'), ###this route will use in the post request of the frontend to register new User
    path('api/users/profile', views.getUserProfile, name = 'user_profile'),
    path('api/furnitures', views.FurnitureList.as_view(), name = 'furniture_list'),
    path('api/furnitures/<int:pk>', views.FurnitureDetail.as_view(), name = 'furniture_detail'),
    path('api/cart', views.FurnitureList.as_view(), name = 'cart_list'),
    path('api/cart/<int:pk>', views.FurnitureDetail.as_view(), name = 'cart_detail'),
    path('api/reviews', views.ReviewList.as_view(), name = 'review_list'),
    path('api/reviews/<int:pk>', views.ReviewDetail.as_view(), name = 'review_detail'),
]

from django.urls import path
from . import views 

urlpatterns = [
    
    path('<int:pk>', views.ProductDetailAPIView.as_view(), name='home'),
    path('', views.ProductListCreateAPIView.as_view(), name='home'),   
    path('<int:pk>/edit', views.ProductUpdateAPIView.as_view(), name='home'),
    path('<int:pk>/delete', views.ProductDeleteAPIView.as_view(), name='home'),

    
    ]



from django.urls import path
from . import views 

urlpatterns = [
    
    path('<int:pk>', views.product_alt_view, name='home'),
    path('', views.product_alt_view, name='home'),    ]


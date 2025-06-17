from django.urls import path
from .views import product_list, HomeView, ProductDetailView

app_name = 'tasks'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', product_list, name='product_list'),
    path('products/', product_list, name='product_list')
]
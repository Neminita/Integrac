from django.contrib import admin
from django.urls import path, include
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('base/', views.base, name='base'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('products/', views.products, name='products'),
    path('carrito/', views.carrito, name='carrito'),
    path('carrito/', views.carrito, name='carrito'),
    path('', include('tasks.urls', namespace='tasks')),
    path('product_list', views.product_list, name='product_list'),

]


from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('products/', views.products, name='products'),
    path('detail_product/', views.detail_product, name='detail_product'),
    path('login_view/', views.LoginView.as_view(), name='login_view'),
    path('register_view/', views.RegisterView.as_view(), name='register_view'),
]

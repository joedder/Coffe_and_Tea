
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    # path('login/', views.login, name='login'),
    # path('register/', views.register, name='register'),
    # path('products/', views.products, name='products'),
    path('detail_product/', views.detail_product, name='detail_product'),
    path('login_view/', views.LoginView.as_view(), name='login_view'),
    path('register_view/', views.RegisterView.as_view(), name='register_view'),
    path('product_view/', views.ProductView.as_view(), name='product_view'),
    path('product_detail_view/<int:id>/', views.ProductDetailView.as_view(), name='product_detail_view'),
    path('comment_detail_view/<int:id>/', views.CommentDetailView.as_view(), name='comment_detail_view'),
    path('comment_update_view/<int:id>/', views.CommentUpdateView.as_view(), name='comment_update_view'),
    path('comment_delete_view/<int:id>/', views.CommentDeleteView.as_view(), name='comment_delete_view'),
    path('logout/', views.UserLogoutView.as_view(), name='logout')
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_list_create_api_view, name='product_create'),
    path('<int:pk>/update/', views.product_update_api_view, name='product_update'),
    path('<int:pk>/delete/', views.product_destroy_api_view, name='product_destroy'),
    path('<int:pk>/', views.product_detail_api_view, name='product_detail'),

]
from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_list_create_api_view, name='product_create'),
    path('<int:pk>/', views.product_detail_api_view, name='product_detail'),

]
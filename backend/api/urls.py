from django.urls import path
from . import views
# from .views import api_home

__name__ = 'api'

urlpatterns = [
    path('', views.api_home, name='api_home'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('devices/', views.device_list, name='device_list'),
    path('devices/add/', views.device_create, name='device_create'),
    path('devices/edit/<int:pk>/', views.device_update, name='device_update'),
    path('devices/delete/<int:pk>/', views.device_delete, name='device_delete'),
]


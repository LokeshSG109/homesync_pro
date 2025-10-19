from django.urls import path
from . import views

urlpatterns = [
    path('', views.renter_list, name='renter_list'),
    path('create/', views.renter_create, name='renter_create'),
]
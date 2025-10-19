from django.urls import path
from . import views

urlpatterns = [
    path('', views.renter_list, name='renter_list'),
    path('create/', views.renter_create, name='renter_create'),
    path('update/<int:pk>/', views.renter_update, name='renter_update'),
    path('delete/<int:pk>/', views.renter_delete, name='renter_delete'),
    path('book/<int:location_id>/', views.book_location, name='book_location'),
    path('bookings/', views.booking_list, name='booking_list'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_view, name='booking_view'),
    path('success/', views.success_view, name='success_view'),
    path('passengers/', views.passenger_list_view, name='passenger_list'), # <--- Add this
]
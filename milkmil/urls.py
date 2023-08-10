from django.urls import path, include
from rest_framework import routers
from milkmil import views


guests_router = routers.SimpleRouter()
guests_router.register('guests', views.GuestsView, basename='guests')

milk_router = routers.SimpleRouter()
milk_router.register('milk', views.MilkView, basename='milk')

vehicle_router = routers.SimpleRouter()
vehicle_router.register('vehicle', views.VehicleView, basename='vehicle')

app_name = 'milkmil'

urlpatterns = [
    path('', include(guests_router.urls)),
    path('', include(milk_router.urls)),
    path('', include(vehicle_router.urls)),
]


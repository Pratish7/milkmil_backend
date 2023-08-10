from django.urls import path, include
from rest_framework import routers
from milkmil import views


guests_router = routers.SimpleRouter()
guests_router.register('guests', views.GuestsView, basename='guests')

app_name = 'milkmil'

urlpatterns = [
    path('', include(guests_router.urls)),
]


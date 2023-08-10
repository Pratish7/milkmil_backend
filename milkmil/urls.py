from django.urls import path, include
from rest_framework import routers
from milkmil import views


guests_router = routers.SimpleRouter()
guests_router.register('guests', views.GuestsView, basename='guests')

milk_router = routers.SimpleRouter()
milk_router.register('milk', views.MilkView, basename='milk')

vehicle_router = routers.SimpleRouter()
vehicle_router.register('vehicle', views.VehicleView, basename='vehicle')

keys_router = routers.SimpleRouter()
keys_router.register('keys', views.KeyView, basename='keys')

returnable_materials_router = routers.SimpleRouter()
returnable_materials_router.register('returnablematerials', views.ReturnableMaterialsView, basename='returnablematerials')

master_data_router = routers.SimpleRouter()
master_data_router.register('masterdata', views.MasterDataView, basename='masterdata')

material_outward_router = routers.SimpleRouter()
material_outward_router.register('materialoutward', views.MaterialOutwardView, basename='materialoutward')

app_name = 'milkmil'

urlpatterns = [
    path('', include(guests_router.urls)),
    path('', include(milk_router.urls)),
    path('', include(vehicle_router.urls)),
    path('', include(keys_router.urls)),
    path('', include(returnable_materials_router.urls)),
    path('', include(master_data_router.urls)),
    path('', include(material_outward_router.urls)),
]

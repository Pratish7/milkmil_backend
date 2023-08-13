from django.urls import path, include
from rest_framework import routers
from milkmil import views


guests_router = routers.SimpleRouter()
guests_router.register('guests', views.GuestsView, basename='guests')

guests_in_router = routers.SimpleRouter()
guests_in_router.register('guests-in', views.GuestsInView, basename='guests-in')

update_guest_out = routers.SimpleRouter()
update_guest_out.register('guest-out', views.GuestsOutUpdateView, basename='guest-out')

guests_report_router = routers.SimpleRouter()
guests_report_router.register('guests-report', views.GuestsReportView, basename='guests-report')

milk_router = routers.SimpleRouter()
milk_router.register('milk', views.MilkView, basename='milk')

milk_report_router = routers.SimpleRouter()
milk_report_router.register('milk-report', views.MilkReportView, basename='milk-report')

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
    path('', include(guests_in_router.urls)),
    path('', include(update_guest_out.urls)),
    path('', include(milk_report_router.urls)),
    path('', include(guests_report_router.urls)),
]

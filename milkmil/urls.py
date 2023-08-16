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

vehicle_report_router = routers.SimpleRouter()
vehicle_report_router.register('vehicle-report', views.VehicleReportView, basename='vehicle-report')

keys_router = routers.SimpleRouter()
keys_router.register('keys', views.KeyView, basename='keys')

keys_report_router = routers.SimpleRouter()
keys_report_router.register('key-report', views.KeyReportView, basename='key-report')

returnable_materials_router = routers.SimpleRouter()
returnable_materials_router.register('returnablematerials', views.ReturnableMaterialsView, basename='returnablematerials')

returnable_materials_queue_router = routers.SimpleRouter()
returnable_materials_queue_router.register('returnablematerials-queue', views.ReturnableMaterialsQueueView, basename='returnablematerials-queue')

returnable_materials_update_router = routers.SimpleRouter()
returnable_materials_update_router.register('returnablematerials-out', views.ReturnableMaterialsUpdateView, basename='returnablematerials-update')

returnable_materials_report_router = routers.SimpleRouter()
returnable_materials_report_router.register('returnablematerials-report', views.ReturnableMaterialsReportView, basename='returnablematerials-report')

master_data_router = routers.SimpleRouter()
master_data_router.register('masterdata', views.MasterDataView, basename='masterdata')

material_inward_router = routers.SimpleRouter()
material_inward_router.register('materialinward', views.MaterialInwardView, basename='materialinward')

material_inward_queue_router = routers.SimpleRouter()
material_inward_queue_router.register('materialinward-queue', views.MaterialInwardQueueView, basename='materialinward-queue')

update_material_inward_router = routers.SimpleRouter()
update_material_inward_router.register('materialinward-out', views.MaterialInwardUpdateView, basename='materialinward-update')

material_inward_report_router = routers.SimpleRouter()
material_inward_report_router.register('materialinward-report', views.MaterialInwardReportView, basename='materialinward-report')

material_outward_router = routers.SimpleRouter()
material_outward_router.register('materialoutward', views.MaterialOutwardView, basename='materialoutward')

material_outward_queue_router = routers.SimpleRouter()
material_outward_queue_router.register('materialoutward-queue', views.MaterialOutwardQueueView, basename='materialoutward-queue')

update_material_outward_router = routers.SimpleRouter()
update_material_outward_router.register('materialoutward-out', views.MaterialOutwardUpdateView, basename='materialoutward-update')

material_outward_report_router = routers.SimpleRouter()
material_outward_report_router.register('materialoutward-report', views.MaterialOutwardReportView, basename='materialoutward-report')

user_types_router = routers.SimpleRouter()
user_types_router.register('usertypes', views.UserTypesView, basename='usertypes')

register_user_router = routers.SimpleRouter()
register_user_router.register('register', views.RegisterUserView, basename='register')

login_user_router = routers.SimpleRouter()
login_user_router.register('login', views.LoginUserView, basename='login')

invoice_bar_router = routers.SimpleRouter()
invoice_bar_router.register('barcode', views.BarCodeView, basename='barcode')

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
    path('', include(vehicle_report_router.urls)),
    path('', include(material_inward_router.urls)),
    path('', include(material_outward_report_router.urls)),
    path('', include(material_inward_report_router.urls)),
    path('', include(returnable_materials_report_router.urls)),
    path('', include(keys_report_router.urls)),
    path('', include(material_inward_queue_router.urls)),
    path('', include(update_material_inward_router.urls)),
    path('', include(material_outward_queue_router.urls)),
    path('', include(update_material_outward_router.urls)),
    path('', include(returnable_materials_queue_router.urls)),
    path('', include(returnable_materials_update_router.urls)),
    path('', include(user_types_router.urls)),
    path('', include(register_user_router.urls)),
    path('', include(login_user_router.urls)),
    path('', include(invoice_bar_router.urls)),
]

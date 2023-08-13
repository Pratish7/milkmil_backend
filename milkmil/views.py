from rest_framework import viewsets, mixins
from milkmil.models import Guests, Milk, Vehicle, Keys, ReturnableMaterials, MasterData, MaterialOutward, MaterialInward
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from milkmil.serializers import GuestsSerializer, MilkSerializer, VehicleSerializer, KeysSerializer, ReturnableMaterialsSerializer, MasterDataSerializer, MaterialOutwardSerializer, MaterialInwardSerializer
from rest_framework.filters import SearchFilter
from milkmil.filters import GuestsFilter, MilkFilter, VehicleFilter, KeyFilter, ReturnableMaterialsFilter, MasterDataFilter, MaterialOutwardFilter, MaterialInwardFilter, GuestsInFilter
from rest_framework import status
from rest_framework.response import Response
from django.utils import timezone


class GuestsView(viewsets.GenericViewSet,  mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = Guests.objects.all()
    serializer_class = GuestsSerializer
    filter_backends = [GuestsFilter, SearchFilter]
    search_fields = ['id', 'visitor_name', 'employee_name', 'relationship', 'in_time', 'out_time']


class MilkView(viewsets.GenericViewSet,  mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = Milk.objects.all()
    serializer_class = MilkSerializer
    filter_backends = [MilkFilter, SearchFilter]
    search_fields = ['id', 'type', 'quantity', 'timestamp']


class VehicleView(viewsets.GenericViewSet,  mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = [VehicleFilter, SearchFilter]
    search_fields = []


class KeyView(viewsets.GenericViewSet,  mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = Keys.objects.all()
    serializer_class = KeysSerializer
    filter_backends = [KeyFilter, SearchFilter]
    search_fields = []


class ReturnableMaterialsView(viewsets.GenericViewSet,  mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = ReturnableMaterials.objects.all()
    serializer_class = ReturnableMaterialsSerializer
    filter_backends = [ReturnableMaterialsFilter, SearchFilter]
    search_fields = []


class MasterDataView(viewsets.GenericViewSet,  mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = MasterData.objects.all()
    serializer_class = MasterDataSerializer
    filter_backends = [MasterDataFilter, SearchFilter]
    search_fields = []


class MaterialOutwardView(viewsets.GenericViewSet,  mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = MaterialOutward.objects.all()
    serializer_class = MaterialOutwardSerializer
    filter_backends = [MaterialOutwardFilter, SearchFilter]
    search_fields = []


class MaterialInwardView(viewsets.GenericViewSet,  mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = MaterialInward.objects.all()
    serializer_class = MaterialInwardSerializer
    filter_backends = [MaterialInwardFilter, SearchFilter]
    search_fields = []


class GuestsInView(viewsets.GenericViewSet,  mixins.ListModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = Guests.objects.all()
    serializer_class = GuestsSerializer
    filter_backends = [GuestsInFilter, SearchFilter]
    search_fields = ['id', 'visitor_name', 'employee_name', 'relationship', 'in_time', 'out_time']


class GuestsOutUpdateView(viewsets.GenericViewSet,  mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = Guests.objects.all()
    serializer_class = GuestsSerializer
    
    def update(self, request, *args, **kwargs):
        
        if 'status' not in request.data or request.data.get('status') != 'out':
            return Response({'status': 'status is required'}, status=status.HTTP_400_BAD_REQUEST)

        instance = self.get_object()
        instance.out_date = timezone.now().date()
        instance.out_time = timezone.now().time()
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

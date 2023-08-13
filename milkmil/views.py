from rest_framework import viewsets, mixins
from milk_mil_backend.users.models import UserTypes
from milkmil.models import Guests, Milk, Vehicle, Keys, ReturnableMaterials, MasterData, MaterialOutward, MaterialInward
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from milkmil.serializers import GuestsSerializer, MilkSerializer, VehicleSerializer, KeysSerializer, ReturnableMaterialsSerializer, MasterDataSerializer, MaterialOutwardSerializer, MaterialInwardSerializer, UserTypesSerializer
from rest_framework.filters import SearchFilter
from milkmil.filters import GuestsFilter, MilkFilter, VehicleFilter, KeyFilter, ReturnableMaterialsFilter, MasterDataFilter, MaterialOutwardFilter, MaterialInwardFilter, GuestsInFilter, MaterialInwardQueueFilter, MaterialOutwardQueueFilter, ReturnableMaterialsQueueFilter
from rest_framework import status
from rest_framework.response import Response
from django.utils import timezone
import pandas as pd
from milkmil.utils import upload_file_to_gcp, generate_download_link
import io


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
    

class MilkReportView(viewsets.GenericViewSet,  mixins.ListModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = Milk.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if 'from_date' not in request.query_params or 'to_date' not in request.query_params:
            return Response({'missing params': 'from_date and to_date are required'}, status=status.HTTP_400_BAD_REQUEST)
        from_date = request.query_params.get('from_date')
        to_date = request.query_params.get('to_date')
        queryset = queryset.filter(date__gte=from_date, date__lte=to_date)
        if not queryset:
            return Response({'message': 'No data found'}, status=status.HTTP_404_NOT_FOUND)
        df = pd.DataFrame.from_records(queryset.values())
        df = df.drop(columns=['id'])
        excel_buffer = io.BytesIO()
        df.to_excel(excel_buffer, index=False)
        excel_buffer.seek(0)
        file_name = f'milk_report_{from_date}_{to_date}.xlsx'
        upload_file_to_gcp(excel_buffer, file_name)
        url = generate_download_link(file_name)
        return Response({'url': url})
    

class GuestsReportView(viewsets.GenericViewSet,  mixins.ListModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = Guests.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if 'from_date' not in request.query_params or 'to_date' not in request.query_params:
            return Response({'missing params': 'from_date and to_date are required'}, status=status.HTTP_400_BAD_REQUEST)
        from_date = request.query_params.get('from_date')
        to_date = request.query_params.get('to_date')
        queryset = queryset.filter(in_date__gte=from_date, in_date__lte=to_date)
        if not queryset:
            return Response({'message': 'No data found'}, status=status.HTTP_404_NOT_FOUND)
        df = pd.DataFrame.from_records(queryset.values())
        df = df.drop(columns=['id'])
        excel_buffer = io.BytesIO()
        df.to_excel(excel_buffer, index=False)
        excel_buffer.seek(0)
        file_name = f'guest_report_{from_date}_{to_date}.xlsx'
        upload_file_to_gcp(excel_buffer, file_name)
        url = generate_download_link(file_name)
        return Response({'url': url})
    

class VehicleReportView(viewsets.GenericViewSet,  mixins.ListModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = Vehicle.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if 'from_date' not in request.query_params or 'to_date' not in request.query_params:
            return Response({'missing params': 'from_date and to_date are required'}, status=status.HTTP_400_BAD_REQUEST)
        from_date = request.query_params.get('from_date')
        to_date = request.query_params.get('to_date')
        queryset = queryset.filter(date__gte=from_date, date__lte=to_date)
        if not queryset:
            return Response({'message': 'No data found'}, status=status.HTTP_404_NOT_FOUND)
        df = pd.DataFrame.from_records(queryset.values())
        excel_buffer = io.BytesIO()
        df.to_excel(excel_buffer, index=False)
        excel_buffer.seek(0)
        file_name = f'vehicle_report_{from_date}_{to_date}.xlsx'
        upload_file_to_gcp(excel_buffer, file_name)
        url = generate_download_link(file_name)
        return Response({'url': url})
    

class MaterialOutwardReportView(viewsets.GenericViewSet,  mixins.ListModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = MaterialOutward.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if 'from_date' not in request.query_params or 'to_date' not in request.query_params:
            return Response({'missing params': 'from_date and to_date are required'}, status=status.HTTP_400_BAD_REQUEST)
        from_date = request.query_params.get('from_date')
        to_date = request.query_params.get('to_date')
        queryset = queryset.filter(date__gte=from_date, date__lte=to_date)
        if not queryset:
            return Response({'message': 'No data found'}, status=status.HTTP_404_NOT_FOUND)
        df = pd.DataFrame.from_records(queryset.values())
        df = df.drop(columns=['id'])
        excel_buffer = io.BytesIO()
        df.to_excel(excel_buffer, index=False)
        excel_buffer.seek(0)
        file_name = f'material_outward_report_{from_date}_{to_date}.xlsx'
        upload_file_to_gcp(excel_buffer, file_name)
        url = generate_download_link(file_name)
        return Response({'url': url})
    

class MaterialInwardReportView(viewsets.GenericViewSet,  mixins.ListModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = MaterialInward.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if 'from_date' not in request.query_params or 'to_date' not in request.query_params:
            return Response({'missing params': 'from_date and to_date are required'}, status=status.HTTP_400_BAD_REQUEST)
        from_date = request.query_params.get('from_date')
        to_date = request.query_params.get('to_date')
        queryset = queryset.filter(date__gte=from_date, date__lte=to_date)
        if not queryset:
            return Response({'message': 'No data found'}, status=status.HTTP_404_NOT_FOUND)
        df = pd.DataFrame.from_records(queryset.values())
        df = df.drop(columns=['id'])
        excel_buffer = io.BytesIO()
        df.to_excel(excel_buffer, index=False)
        excel_buffer.seek(0)
        file_name = f'material_inward_report_{from_date}_{to_date}.xlsx'
        upload_file_to_gcp(excel_buffer, file_name)
        url = generate_download_link(file_name)
        return Response({'url': url})
    

class ReturnableMaterialsReportView(viewsets.GenericViewSet,  mixins.ListModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = ReturnableMaterials.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if 'from_date' not in request.query_params or 'to_date' not in request.query_params:
            return Response({'missing params': 'from_date and to_date are required'}, status=status.HTTP_400_BAD_REQUEST)
        from_date = request.query_params.get('from_date')
        to_date = request.query_params.get('to_date')
        queryset = queryset.filter(out_date__gte=from_date, out_date__lte=to_date)
        if not queryset:
            return Response({'message': 'No data found'}, status=status.HTTP_404_NOT_FOUND)
        df = pd.DataFrame.from_records(queryset.values())
        df = df.drop(columns=['id'])
        excel_buffer = io.BytesIO()
        df.to_excel(excel_buffer, index=False)
        excel_buffer.seek(0)
        file_name = f'returnable_material_report_{from_date}_{to_date}.xlsx'
        upload_file_to_gcp(excel_buffer, file_name)
        url = generate_download_link(file_name)
        return Response({'url': url})
    

class KeyReportView(viewsets.GenericViewSet,  mixins.ListModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = Keys.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if 'from_date' not in request.query_params or 'to_date' not in request.query_params:
            return Response({'missing params': 'from_date and to_date are required'}, status=status.HTTP_400_BAD_REQUEST)
        from_date = request.query_params.get('from_date')
        to_date = request.query_params.get('to_date')
        queryset = queryset.filter(date__gte=from_date, date__lte=to_date)
        if not queryset:
            return Response({'message': 'No data found'}, status=status.HTTP_404_NOT_FOUND)
        df = pd.DataFrame.from_records(queryset.values())
        df = df.drop(columns=['id'])
        excel_buffer = io.BytesIO()
        df.to_excel(excel_buffer, index=False)
        excel_buffer.seek(0)
        file_name = f'key_report_{from_date}_{to_date}.xlsx'
        upload_file_to_gcp(excel_buffer, file_name)
        url = generate_download_link(file_name)
        return Response({'url': url})


class MaterialInwardQueueView(viewsets.GenericViewSet,  mixins.ListModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = MaterialInward.objects.all()
    serializer_class = MaterialInwardSerializer
    filter_backends = [MaterialInwardQueueFilter, SearchFilter]


class MaterialInwardUpdateView(viewsets.GenericViewSet,  mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = MaterialInward.objects.all()
    serializer_class = MaterialInwardSerializer
    
    def update(self, request, *args, **kwargs):
        
        if 'status' not in request.data or request.data.get('status') != 'out':
            return Response({'status': 'status is required'}, status=status.HTTP_400_BAD_REQUEST)

        instance = self.get_object()
        instance.out_time = timezone.now().time()
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    

class MaterialOutwardQueueView(viewsets.GenericViewSet,  mixins.ListModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = MaterialOutward.objects.all()
    serializer_class = MaterialOutwardSerializer
    filter_backends = [MaterialOutwardQueueFilter, SearchFilter]


class MaterialOutwardUpdateView(viewsets.GenericViewSet,  mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = MaterialOutward.objects.all()
    serializer_class = MaterialOutwardSerializer
    
    def update(self, request, *args, **kwargs):
        
        if 'status' not in request.data or request.data.get('status') != 'out':
            return Response({'status': 'status is required'}, status=status.HTTP_400_BAD_REQUEST)

        instance = self.get_object()
        instance.status = 'DISPATCHED / COMPLETED'
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    

class ReturnableMaterialsQueueView(viewsets.GenericViewSet,  mixins.ListModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = ReturnableMaterials.objects.all()
    serializer_class = ReturnableMaterialsSerializer
    filter_backends = [ReturnableMaterialsQueueFilter, SearchFilter]


class ReturnableMaterialsUpdateView(viewsets.GenericViewSet,  mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = ReturnableMaterials.objects.all()
    serializer_class = ReturnableMaterialsSerializer
    
    def update(self, request, *args, **kwargs):
        
        if 'status' not in request.data or request.data.get('status') != 'out':
            return Response({'status': 'status is required'}, status=status.HTTP_400_BAD_REQUEST)

        instance = self.get_object()
        instance.status = 'RETURNED / COMPLETED'
        instance.in_date = timezone.now().date()
        instance.in_time = timezone.now().time()
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    

class UserTypesView(mixins.ListModelMixin, viewsets.GenericViewSet):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = UserTypes.objects.all()
    serializer_class = UserTypesSerializer

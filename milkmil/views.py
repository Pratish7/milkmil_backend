from rest_framework import viewsets, mixins
from milk_mil_backend.users.models import UserTypes
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from milkmil.models import BarCode, Employees, Guests, KeysMaster, Milk, Vehicle, Keys, ReturnableMaterials, MasterData, MaterialOutward, MaterialInward
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from milkmil.permissions import CanViewReport, CanWriteGuest, CanWriteKeys, CanWriteMasterData, CanWriteMaterialInward, CanWriteMaterialOutward, CanWriteMilk, CanWriteReturnableMaterials, CanWriteVehicle
from milkmil.serializers import BarCodeSerializer, EmployeeSerializer, GuestsSerializer, KeyMasterSerializer, MilkSerializer, VehicleSerializer, KeysSerializer, ReturnableMaterialsSerializer, MasterDataSerializer, MaterialOutwardSerializer, MaterialInwardSerializer, UserTypesSerializer, RegisterUserSerializer, LoginUserSerializer
from rest_framework.filters import SearchFilter
from milkmil.filters import GuestsFilter, KeysQueue, MilkFilter, VehicleFilter, KeyFilter, ReturnableMaterialsFilter, MasterDataFilter, MaterialOutwardFilter, MaterialInwardFilter, GuestsInFilter, MaterialInwardQueueFilter, MaterialOutwardQueueFilter, ReturnableMaterialsQueueFilter
from rest_framework import status
from rest_framework.response import Response
import pandas as pd
from milkmil.utils import upload_file_to_gcp, generate_download_link, upload_key_file_to_gcp, generate_key_download_link
import io
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from barcode.writer import ImageWriter
from io import BytesIO
import base64
import barcode
from datetime import date


class GuestsView(viewsets.GenericViewSet,  mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = Guests.objects.all()
    serializer_class = GuestsSerializer
    filter_backends = [GuestsFilter, SearchFilter]


class MilkView(viewsets.GenericViewSet,  mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = (IsAuthenticated, CanWriteMilk)
    queryset = Milk.objects.all()
    serializer_class = MilkSerializer
    filter_backends = [MilkFilter, SearchFilter]


class VehicleView(viewsets.GenericViewSet,  mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = (IsAuthenticated, CanWriteVehicle)
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = [VehicleFilter, SearchFilter]


class KeyView(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = (IsAuthenticated, CanWriteKeys)
    queryset = Keys.objects.all()
    serializer_class = KeysSerializer
    filter_backends = [KeyFilter, SearchFilter]


class ReturnableMaterialsView(viewsets.GenericViewSet,  mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = (IsAuthenticated, CanWriteReturnableMaterials)
    queryset = ReturnableMaterials.objects.all()
    serializer_class = ReturnableMaterialsSerializer
    filter_backends = [ReturnableMaterialsFilter, SearchFilter]


class MasterDataView(viewsets.GenericViewSet,  mixins.ListModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = MasterData.objects.all()
    serializer_class = MasterDataSerializer
    filter_backends = [MasterDataFilter, SearchFilter]
    search_fields = []


class MasterDataUpdateView(viewsets.GenericViewSet,  mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = (IsAuthenticated, CanWriteMasterData)
    queryset = MasterData.objects.all()
    serializer_class = MasterDataSerializer

    def update(self, request, *args, **kwargs):

        pk = kwargs.get('pk')
        obj = MasterData.objects.get(key=pk)
        if not obj:
            return Response({'message': 'Invalid key'}, status=status.HTTP_400_BAD_REQUEST)

        if request.data['name'] not in obj.values:
            obj.values.append(request.data['name'])
            obj.save()

        return Response({'message': 'success'})


class MaterialOutwardView(viewsets.GenericViewSet,  mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = (IsAuthenticated, CanWriteMaterialOutward)
    queryset = MaterialOutward.objects.all()
    serializer_class = MaterialOutwardSerializer
    filter_backends = [MaterialOutwardFilter, SearchFilter]


class MaterialInwardView(viewsets.GenericViewSet,  mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = (IsAuthenticated, CanWriteMaterialInward)
    queryset = MaterialInward.objects.all()
    serializer_class = MaterialInwardSerializer
    filter_backends = [MaterialInwardFilter, SearchFilter]


class GuestsInView(viewsets.GenericViewSet,  mixins.ListModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = Guests.objects.all()
    serializer_class = GuestsSerializer
    filter_backends = [GuestsInFilter, SearchFilter]
    search_fields = ['id', 'visitor_name', 'employee_name', 'relationship', 'in_time', 'out_time']


class GuestsOutUpdateView(viewsets.GenericViewSet,  mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = (IsAuthenticated, CanWriteGuest)
    queryset = Guests.objects.all()
    serializer_class = GuestsSerializer
    
    def update(self, request, *args, **kwargs):
        
        if 'status' not in request.data or request.data.get('status') != 'out':
            return Response({'status': 'status is required'}, status=status.HTTP_400_BAD_REQUEST)

        instance = self.get_object()
        instance.out_date = request.ist_now.date()
        instance.out_time = request.ist_now.time()
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    

class MilkReportView(viewsets.GenericViewSet,  mixins.ListModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = (IsAuthenticated, CanViewReport)
    queryset = Milk.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if 'from_date' not in request.query_params or 'to_date' not in request.query_params:
            return Response({'missing params': 'from_date and to_date are required'}, status=status.HTTP_400_BAD_REQUEST)
        from_date = request.query_params.get('from_date')
        to_date = request.query_params.get('to_date')
        queryset = queryset.filter(date__gte=from_date, date__lte=to_date)
        if not queryset:
            df = pd.DataFrame()
        else:
            df = pd.DataFrame.from_records(queryset.values())
            df['date'] = pd.to_datetime(df['date']).dt.strftime("%d-%m-%Y")
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
    permission_classes = (IsAuthenticated, CanViewReport)
    queryset = Guests.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if 'from_date' not in request.query_params or 'to_date' not in request.query_params:
            return Response({'missing params': 'from_date and to_date are required'}, status=status.HTTP_400_BAD_REQUEST)
        from_date = request.query_params.get('from_date')
        to_date = request.query_params.get('to_date')
        queryset = queryset.filter(in_date__gte=from_date, in_date__lte=to_date)
        if not queryset:
            df = pd.DataFrame()
        else:
            df = pd.DataFrame.from_records(queryset.values())
            df = df.drop(columns=['id', 'image'])
            df['in_date'] = pd.to_datetime(df['in_date']).dt.strftime("%d-%m-%Y")
            df['out_date'] = pd.to_datetime(df['out_date']).dt.strftime("%d-%m-%Y")
        excel_buffer = io.BytesIO()
        df.to_excel(excel_buffer, index=False)
        excel_buffer.seek(0)
        file_name = f'guest_report_{from_date}_{to_date}.xlsx'
        upload_file_to_gcp(excel_buffer, file_name)
        url = generate_download_link(file_name)
        return Response({'url': url})
    

class VehicleReportView(viewsets.GenericViewSet,  mixins.ListModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = (IsAuthenticated, CanViewReport)
    queryset = Vehicle.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if 'from_date' not in request.query_params or 'to_date' not in request.query_params:
            return Response({'missing params': 'from_date and to_date are required'}, status=status.HTTP_400_BAD_REQUEST)
        from_date = request.query_params.get('from_date')
        to_date = request.query_params.get('to_date')
        queryset = queryset.filter(date__gte=from_date, date__lte=to_date)
        if not queryset:
            df = pd.DataFrame()
        else:
            df = pd.DataFrame.from_records(queryset.values())
            df['date'] = pd.to_datetime(df['date']).dt.strftime("%d-%m-%Y")
        excel_buffer = io.BytesIO()
        df.to_excel(excel_buffer, index=False)
        excel_buffer.seek(0)
        file_name = f'vehicle_report_{from_date}_{to_date}.xlsx'
        upload_file_to_gcp(excel_buffer, file_name)
        url = generate_download_link(file_name)
        return Response({'url': url})
    

class MaterialOutwardReportView(viewsets.GenericViewSet,  mixins.ListModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = (IsAuthenticated, CanViewReport)
    queryset = MaterialOutward.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if 'from_date' not in request.query_params or 'to_date' not in request.query_params:
            return Response({'missing params': 'from_date and to_date are required'}, status=status.HTTP_400_BAD_REQUEST)
        from_date = request.query_params.get('from_date')
        to_date = request.query_params.get('to_date')
        queryset = queryset.filter(date__gte=from_date, date__lte=to_date)
        if not queryset:
            df = pd.DataFrame()
        else:
            df = pd.DataFrame.from_records(queryset.values())
            df['date'] = pd.to_datetime(df['date']).dt.strftime("%d-%m-%Y")
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
    permission_classes = (IsAuthenticated, CanViewReport)
    queryset = MaterialInward.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if 'from_date' not in request.query_params or 'to_date' not in request.query_params:
            return Response({'missing params': 'from_date and to_date are required'}, status=status.HTTP_400_BAD_REQUEST)
        from_date = request.query_params.get('from_date')
        to_date = request.query_params.get('to_date')
        queryset = queryset.filter(date__gte=from_date, date__lte=to_date)
        if not queryset:
            df = pd.DataFrame()
        else:
            df = pd.DataFrame.from_records(queryset.values())
            df['date'] = pd.to_datetime(df['date']).dt.strftime("%d-%m-%Y")
            df = df.drop(columns=['id', 'image'])
        excel_buffer = io.BytesIO()
        df.to_excel(excel_buffer, index=False)
        excel_buffer.seek(0)
        file_name = f'material_inward_report_{from_date}_{to_date}.xlsx'
        upload_file_to_gcp(excel_buffer, file_name)
        url = generate_download_link(file_name)
        return Response({'url': url})
    

class ReturnableMaterialsReportView(viewsets.GenericViewSet,  mixins.ListModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = (IsAuthenticated, CanViewReport)
    queryset = ReturnableMaterials.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if 'from_date' not in request.query_params or 'to_date' not in request.query_params:
            return Response({'missing params': 'from_date and to_date are required'}, status=status.HTTP_400_BAD_REQUEST)
        from_date = request.query_params.get('from_date')
        to_date = request.query_params.get('to_date')
        queryset = queryset.filter(out_date__gte=from_date, out_date__lte=to_date)
        if not queryset:
            df = pd.DataFrame()
        else:
            df = pd.DataFrame.from_records(queryset.values())
            df['in_date'] = pd.to_datetime(df['in_date']).dt.strftime("%d-%m-%Y")
            df['out_date'] = pd.to_datetime(df['out_date']).dt.strftime("%d-%m-%Y")
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
    permission_classes = (IsAuthenticated, CanViewReport)
    queryset = Keys.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if 'from_date' not in request.query_params or 'to_date' not in request.query_params:
            return Response({'missing params': 'from_date and to_date are required'}, status=status.HTTP_400_BAD_REQUEST)
        from_date = request.query_params.get('from_date')
        to_date = request.query_params.get('to_date')
        queryset = queryset.filter(date__gte=from_date, date__lte=to_date)
        if not queryset:
            df = pd.DataFrame()
        else:
            df = pd.DataFrame.from_records(queryset.values())
            df = df.drop(columns=['id'])
            df['date'] = pd.to_datetime(df['date']).dt.strftime("%d-%m-%Y")
        excel_buffer = io.BytesIO()
        df.to_excel(excel_buffer, index=False)
        excel_buffer.seek(0)
        file_name = f'key_report_{from_date}_{to_date}.xlsx'
        upload_file_to_gcp(excel_buffer, file_name)
        url = generate_download_link(file_name)
        return Response({'url': url})


class MaterialInwardQueueView(viewsets.GenericViewSet,  mixins.ListModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = (IsAuthenticated, CanWriteMaterialInward)
    queryset = MaterialInward.objects.all()
    serializer_class = MaterialInwardSerializer
    filter_backends = [MaterialInwardQueueFilter, SearchFilter]


class MaterialInwardUpdateView(viewsets.GenericViewSet,  mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = (IsAuthenticated, CanWriteMaterialInward)
    queryset = MaterialInward.objects.all()
    serializer_class = MaterialInwardSerializer
    
    def update(self, request, *args, **kwargs):
        
        if 'status' not in request.data or request.data.get('status') != 'out':
            return Response({'status': 'status is required'}, status=status.HTTP_400_BAD_REQUEST)

        instance = self.get_object()
        instance.out_time = request.ist_now.time()
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    

class MaterialOutwardQueueView(viewsets.GenericViewSet,  mixins.ListModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = (IsAuthenticated, CanWriteMaterialOutward)
    queryset = MaterialOutward.objects.all()
    serializer_class = MaterialOutwardSerializer
    filter_backends = [MaterialOutwardQueueFilter, SearchFilter]


class MaterialOutwardUpdateView(viewsets.GenericViewSet,  mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = (IsAuthenticated, CanWriteMaterialOutward)
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
    permission_classes = (IsAuthenticated, CanWriteReturnableMaterials)
    queryset = ReturnableMaterials.objects.all()
    serializer_class = ReturnableMaterialsSerializer
    filter_backends = [ReturnableMaterialsQueueFilter, SearchFilter]


class ReturnableMaterialsUpdateView(viewsets.GenericViewSet,  mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = (IsAuthenticated, CanWriteReturnableMaterials)
    queryset = ReturnableMaterials.objects.all()
    serializer_class = ReturnableMaterialsSerializer
    
    def update(self, request, *args, **kwargs):
        
        if 'status' not in request.data or request.data.get('status') != 'out':
            return Response({'status': 'status is required'}, status=status.HTTP_400_BAD_REQUEST)

        instance = self.get_object()
        instance.status = 'RETURNED / COMPLETED'
        instance.in_date = request.ist_now.date()
        instance.in_time = request.ist_now.time()
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    

class UserTypesView(mixins.ListModelMixin, viewsets.GenericViewSet):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = UserTypes.objects.all()
    serializer_class = UserTypesSerializer


class RegisterUserView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = get_user_model().objects.all()
    serializer_class = RegisterUserSerializer


class LoginUserView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = get_user_model().objects.all()
    serializer_class = LoginUserSerializer

    def create(self, request, *args, **kwargs):

        req_data = request.data
        if 'email' not in req_data or 'password' not in req_data:
            return Response({'message': 'email and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=req_data['email'], password=req_data['password'])
        if not user:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        token = Token.objects.get_or_create(user=user)[0]
        user_data = {}
        user_data['id'] = user.id
        user_data['email'] = user.email
        user_data['name'] = user.name

        user_permissions = []
        perms = UserTypes.objects.filter(user=user)
        for i in perms:
            user_permissions.append(i.user_type)
        user_data['user_type'] = user_permissions

        if user.is_superuser:
            user_data['user_type'] = ['superadmin']

        return Response({'auth_token': token.key, 'user': user_data})


class BarCodeView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = BarCode.objects.all()
    serializer_class = BarCodeSerializer

    def create(self, request, *args, **kwargs):

        bar_code_last_suffix = BarCode.objects.last()
        if not bar_code_last_suffix:
            bar_code_last_suffix = 1000
        else:
            if bar_code_last_suffix.invoice_num[:8] != str(date.today()).replace('-', ''):
                bar_code_last_suffix = 1000
            else:
                bar_code_last_suffix = int(bar_code_last_suffix.invoice_num[-4:])

        barcode_value = str(date.today()).replace('-', '') + str(bar_code_last_suffix + 1)
        barcode_image = barcode.get('ean13', barcode_value, writer=ImageWriter())
        buffer = BytesIO()
        barcode_image.write(buffer)
        # base64_image = base64.b64encode(buffer.getvalue()).decode('utf-8')
        # BarCode.objects.create(invoice_num=barcode_value, barcode=base64_image).save()
        upload_key_file_to_gcp(buffer.getvalue(), barcode_value, 'invoice_bar_code')
        url = generate_key_download_link(barcode_value, 'invoice_bar_code')
        return Response({'url': url, 'value': barcode_value}, status=status.HTTP_201_CREATED)


class CreateKeyView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = (IsAuthenticated, CanWriteMasterData)
    queryset = KeysMaster.objects.all()
    serializer_class = KeyMasterSerializer

    def create(self, request, *args, **kwargs):
        barcode_value = request.data.get('key_type')

        if KeysMaster.objects.filter(key_type=barcode_value):
            return Response({'message': 'Key already exists'}, status=status.HTTP_400_BAD_REQUEST)

        barcode_image = barcode.get('code128', barcode_value, writer=ImageWriter())
        buffer = BytesIO()
        barcode_image.write(buffer)
        # base64_image = base64.b64encode(buffer.getvalue()).decode('utf-8')
        # KeysMaster.objects.create(key_type=barcode_value, bar_code=base64_image, quantity=request.data.get('quantity')).save()
        upload_key_file_to_gcp(buffer.getvalue(), barcode_value, 'key_bar_code')
        url = generate_key_download_link(barcode_value, 'key_bar_code')
        return Response({'url': url}, status=status.HTTP_201_CREATED)
    

class GuestsSuggestionsView(viewsets.GenericViewSet, mixins.ListModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = Guests.objects.all()
    serializer_class = GuestsSerializer

    def list(self, request):
        guests = Guests.objects.values_list('visitor_name', flat=True).distinct()
        return Response({'guests': guests})


class EmployeeCreateView(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = (IsAuthenticated, CanWriteMasterData)
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeView(viewsets.GenericViewSet, mixins.ListModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = (IsAuthenticated, CanWriteKeys)
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [SearchFilter]


class KeyQueueView(viewsets.GenericViewSet,  mixins.ListModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = (IsAuthenticated, CanWriteKeys)
    queryset = Keys.objects.all()
    serializer_class = KeysSerializer
    filter_backends = [KeysQueue, SearchFilter]


class UpdateKeyReturnedView(viewsets.GenericViewSet, mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = (IsAuthenticated, CanWriteKeys)
    queryset = Keys.objects.all()
    serializer_class = KeysSerializer
    filter_backends = [KeysQueue, SearchFilter]


class KeyReturnedUpdateView(viewsets.GenericViewSet,  mixins.UpdateModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = (IsAuthenticated, CanWriteKeys)
    queryset = Keys.objects.all()
    serializer_class = KeysSerializer
    
    def update(self, request, *args, **kwargs):
        
        if 'status' not in request.data or request.data.get('status') != 'returned':
            return Response({'status': 'status is required'}, status=status.HTTP_400_BAD_REQUEST)
        instance = self.get_object()
        instance.returned_time = request.ist_now.time()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
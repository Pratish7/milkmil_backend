from rest_framework import serializers
from milk_mil_backend.users.models import UserTypes
from milkmil.models import Guests, Milk, Vehicle, Keys, ReturnableMaterials, MasterData, MaterialOutward, MaterialInward
from django.contrib.auth import get_user_model

class GuestsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guests
        fields = '__all__'
        read_only_fields = ['id', 'in_date', 'in_time', 'out_date', 'out_time']


class MilkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Milk
        fields = '__all__'
        read_only_fields = ['id', 'date', 'time']


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = '__all__'
        read_only_fields = ['id', 'date', 'in_time', 'out_time']


class KeysSerializer(serializers.ModelSerializer):

    class Meta:
        model = Keys
        fields = '__all__'
        read_only_fields = ['id']


class ReturnableMaterialsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReturnableMaterials
        fields = '__all__'
        read_only_fields = ['id', 'date', 'in_date', 'in_time', 'out_date', 'out_time', 'status']


class MasterDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = MasterData
        fields = '__all__'


class MaterialOutwardSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaterialOutward
        fields = '__all__'
        read_only_fields = ['id', 'date', 'time', 'status']


class MaterialInwardSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaterialInward
        fields = '__all__'
        read_only_fields = ['id', 'date', 'in_time']

    
class UserTypesSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserTypes
        fields = '__all__'
        read_only_fields = ['id']


class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['id', 'name', 'user_type', 'email']


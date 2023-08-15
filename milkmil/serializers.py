from rest_framework import serializers
from milk_mil_backend.users.models import UserTypes
from milkmil.models import Guests, Milk, Vehicle, Keys, ReturnableMaterials, MasterData, MaterialOutward, MaterialInward
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


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
        fields = '__all__'

    def create(self, validated_data):
        if 'user_type' in validated_data:
            user_types = validated_data.pop('user_type')
            print(validated_data)
        validated_data['password'] = make_password(validated_data['password'])
        user = get_user_model().objects.create(**validated_data)
        for user_type in user_types:
            user.user_type.add(user_type)
        return user


class LoginUserSerializer(serializers.ModelSerializer):

    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        user_permissions = []
        perms = UserTypes.objects.filter(user=user)
        for i in perms:
            user_permissions.append(i.user_type)
        token['user_type'] = user_permissions
        token['name'] = user.name
        token['email'] = user.email
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        return data

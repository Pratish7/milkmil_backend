from rest_framework import serializers
from milkmil.models import Guests, Milk, Vehicle, Keys, ReturnableMaterials, MasterData


class GuestsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guests
        fields = '__all__'


class MilkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Milk
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = '__all__'


class KeysSerializer(serializers.ModelSerializer):

    class Meta:
        model = Keys
        fields = '__all__'


class ReturnableMaterialsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReturnableMaterials
        fields = '__all__'


class MasterDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = MasterData
        fields = '__all__'

from rest_framework import serializers
from milkmil.models import Guests, Milk, Vehicle, Keys


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
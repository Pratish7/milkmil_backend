from rest_framework import serializers
from milkmil.models import Guests, Milk, Vehicle


class GuestsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guests
        fields = '__all__'

        def create(self, validated_data):
            return super().create(validated_data)
        

class MilkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Milk
        fields = '__all__'

        def create(self, validated_data):
            return super().create(validated_data)
        

class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = '__all__'

        def create(self, validated_data):
            return super().create(validated_data)
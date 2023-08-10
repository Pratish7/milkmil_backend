from rest_framework import serializers
from milkmil.models import Guests


class GuestsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guests
        fields = '__all__'

        def create(self, validated_data):
            return super().create(validated_data)
        
        
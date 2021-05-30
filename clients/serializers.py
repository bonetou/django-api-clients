from django.db.models import fields
from rest_framework import serializers
from clients.models import Client
from clients.validators import *

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def validate(self, data):
        if not name_valid(data['name']):
            raise serializers.ValidationError({'name': 'Name must be alphabetical'})
        if not cpf_valid(data['cpf']):
            raise serializers.ValidationError({'id_number': 'CPF is not valid'})
        if not phone_number_valid(data['phone_number']):
            raise serializers.ValidationError({'phone_number': 'Must have follow the pattern: 11 12345-1234'})
        return data
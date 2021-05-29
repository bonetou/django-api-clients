from django.db.models import fields
from rest_framework import serializers
from clients.models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def validate_id_number(self, id_number):
        if id_number != 11:
            raise serializers.ValidationError("id_number must have 11 characters")
        return id_number
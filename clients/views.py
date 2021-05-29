from rest_framework import viewsets
from clients.models import Client
from clients.serializers import ClientSerializer

class ClientViewSet(viewsets.ModelViewSet):
    '''List clients'''
    queryset = Client.objects.all()
    serializer_class = ClientSerializer



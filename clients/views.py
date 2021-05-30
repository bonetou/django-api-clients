from rest_framework import viewsets, filters
from clients.models import Client
from clients.serializers import ClientSerializer
from django_filters.rest_framework import DjangoFilterBackend, filterset

class ClientViewSet(viewsets.ModelViewSet):
    '''List clients'''
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends  = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name', 'cpf']
    filterset_fields = ['active']
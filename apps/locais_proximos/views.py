
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.locais_proximos.models import LocaisProximos
from .serializers import LocaisProximosSerializer

class LocaisProximosViewSet(viewsets.ModelViewSet):
    permission_classes = []  # Permite acesso público
    serializer_class = LocaisProximosSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description']

    def get_queryset(self):
        # Obtém o ID do media_item da query string
        media_item_id = self.request.query_params.get('media_item')
        
        # Se houver um media_item_id, filtra apenas os locais daquele item
        if media_item_id:
            return LocaisProximos.objects.filter(media_item_id=media_item_id)
            
        # Se não houver media_item_id na query, retorna queryset vazio
        return LocaisProximos.objects.none()
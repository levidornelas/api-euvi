from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.media_items.models import MediaItem
from .serializers import MediaItemSerializer, LocaisProximosSerializer
from .mixins.itens_salvos import ItensSalvosMixin

class MediaItemViewSet(viewsets.ModelViewSet, ItensSalvosMixin):
    permission_classes = []
    queryset = MediaItem.objects.prefetch_related('locais')
    serializer_class = MediaItemSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'location', 'general_info', 'media_type']
    
    def retrieve(self, request, pk=None):
        try:
            item = self.queryset.get(pk=pk)
            serializer = self.get_serializer(item)
            data = serializer.data
            
            locais = item.locais.all()
            locais_serializer = LocaisProximosSerializer(locais, many=True)
            data['locais'] = locais_serializer.data
            
            return Response(data)
        except MediaItem.DoesNotExist:
            return Response({'error': 'Item não encontrado'}, status=404)
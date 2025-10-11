from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from apps.media_items.models import MediaItem
from apps.api.mixins import ReadAuthenticatedWriteAdminMixin
from .serializers import MediaItemSerializer, LocaisProximosSerializer
from .mixins.itens_salvos import ItensSalvosMixin


class MediaItemViewSet(
    ReadAuthenticatedWriteAdminMixin,
    ItensSalvosMixin,
    viewsets.ModelViewSet
):
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

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ItensSalvosMixin():
    @action(detail=True, methods=['post'], permission_classes=[])
    def salvar(self, request, pk=None):
        """Salva um local para o usuário autenticado"""
        media_item = self.get_object()
        user = request.user
        
        if media_item in user.locais_salvos.all():
            return Response(
                {'detail': 'Local já está salvo.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user.locais_salvos.add(media_item)
        return Response(
            {'detail': 'Local salvo com sucesso.'},
            status=status.HTTP_200_OK
        )
    
    @action(detail=True, methods=['post'], permission_classes=[])
    def remover(self, request, pk=None):
        """Remove um local salvo do usuário autenticado"""
        media_item = self.get_object()
        user = request.user
        
        if media_item not in user.locais_salvos.all():
            return Response(
                {'detail': 'Local não está salvo.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user.locais_salvos.remove(media_item)
        return Response(
            {'detail': 'Local removido com sucesso.'},
            status=status.HTTP_200_OK
        )
    

    @action(detail=True, methods=['get'], permission_classes=[])
    def esta_salvo(self, request, pk=None):
        """Verifica se o local está salvo pelo usuário"""
        media_item = self.get_object()
        esta_salvo = media_item in request.user.locais_salvos.all()
        return Response({'esta_salvo': esta_salvo})
    

    @action(detail=False, methods=['get'], permission_classes=[])
    def meus_salvos(self, request):
        """Lista todos os locais salvos pelo usuário"""
        locais_salvos = request.user.locais_salvos.all()
        serializer = self.get_serializer(locais_salvos, many=True)
        return Response(serializer.data)
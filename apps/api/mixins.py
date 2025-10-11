from rest_framework.permissions import IsAuthenticated, IsAdminUser


class ReadAuthenticatedWriteAdminMixin:
    """
    Mixin que permite leitura (GET) para usuários autenticados
    e escrita (POST, PUT, PATCH, DELETE) apenas para administradores.
    """
    
    def get_permissions(self):
        """
        Define permissões diferentes para cada ação
        """
        if self.action in ['list', 'retrieve']:
            # GET (lista e detalhes) requer apenas autenticação
            permission_classes = [IsAuthenticated]
        elif self.action in ['create', 'update', 'partial_update', 'destroy']:
            # POST, PUT, PATCH, DELETE requerem admin
            permission_classes = [IsAdminUser]
        else:
            # Fallback para ações customizadas
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .serializers import (
    UserSerializer,
    RegisterSerializer,
    ChangePasswordSerializer,
    UpdateProfileSerializer
)

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    """View para registro de novo usuário"""
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    @swagger_auto_schema(
        tags=['Auth'],
        operation_description="Registra um novo usuário e retorna tokens JWT"
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'user': UserSerializer(user).data,
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            },
            'message': 'Usuário registrado com sucesso!'
        }, status=status.HTTP_201_CREATED)


class LogoutView(APIView):
    """View para logout (blacklist do refresh token)"""
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=['Auth'],
    )
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            if not refresh_token:
                return Response(
                    {"error": "Refresh token é obrigatório."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            token = RefreshToken(refresh_token)
            token.blacklist()
            
            return Response(
                {"message": "Logout realizado com sucesso."},
                status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {"error": "Token inválido ou expirado."},
                status=status.HTTP_400_BAD_REQUEST
            )


class UserProfileView(generics.RetrieveUpdateAPIView):
    """View para visualizar e atualizar perfil do usuário"""
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    @swagger_auto_schema(
        tags=['Auth'],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Auth'],
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Auth'],
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        serializer = UpdateProfileSerializer(
            self.get_object(),
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({
            'user': UserSerializer(self.get_object()).data,
            'message': 'Perfil atualizado com sucesso!'
        })


class CustomTokenObtainPairView(TokenObtainPairView):
    @swagger_auto_schema(
        tags=['Auth'],
        operation_id='auth_login',
        operation_description='Obtém tokens de acesso e refresh'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CustomTokenRefreshView(TokenRefreshView):
    @swagger_auto_schema(
        tags=['Auth'],
        operation_id='auth_token_refresh',
        operation_description='Atualiza o token de acesso usando o refresh token'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
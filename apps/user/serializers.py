from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer para dados do usuário"""
    class Meta:
        model = User
        fields = ('uuid', 'username', 'email', 'first_name',
                  'last_name', 'bio', 'avatar')
        read_only_fields = ('uuid',)


class RegisterSerializer(serializers.ModelSerializer):

    """Serializer para registro de novo usuário"""
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
        label='Confirmar senha'
    )

    class Meta:
        model = User
        fields = ('email', 'password', 'password2', 'first_name', 'last_name')
        extra_kwargs = {
            'username': {'required': False},
            'first_name': {'required': False},
            'last_name': {'required': False}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({
                "password": "As senhas não coincidem."
            })
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user


class ChangePasswordSerializer(serializers.Serializer):
    """Serializer para alteração de senha"""
    old_password = serializers.CharField(
        required=True,
        style={'input_type': 'password'}
    )
    new_password = serializers.CharField(
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )


class UpdateProfileSerializer(serializers.ModelSerializer):
    """Serializer para atualização de perfil"""
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'bio', 'avatar')


class SocialLoginSerializer(serializers.Serializer):
    """Serializer base para login social"""
    access_token = serializers.CharField(
        required=True,
        help_text="Access token obtido do provider OAuth2"
    )

    def validate_access_token(self, value):
        if not value:
            raise serializers.ValidationError("Access token é obrigatório.")
        return value


class SocialAuthResponseSerializer(serializers.Serializer):
    """Serializer para resposta de autenticação social"""
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    user = UserSerializer(read_only=True)

    def create_tokens_response(self, user):
        """Cria a resposta com tokens JWT e dados do usuário"""
        from rest_framework_simplejwt.tokens import RefreshToken

        refresh = RefreshToken.for_user(user)

        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'user': UserSerializer(user).data
        }


class GoogleLoginSerializer(SocialLoginSerializer):
    """Serializer específico para login com Google"""

    def get_user_from_social_account(self):
        """Obtém o usuário autenticado pelo Google"""
        from allauth.socialaccount.models import SocialAccount

        try:
            social_account = SocialAccount.objects.filter(
                provider='google'
            ).select_related('user').latest('id')
            return social_account.user
        except SocialAccount.DoesNotExist:
            raise serializers.ValidationError(
                "Não foi possível autenticar com o Google. Verifique o token."
            )

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.media_items.views import MediaItemViewSet
from apps.locais_proximos.views import LocaisProximosViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.user.views import (
    RegisterView, 
    LogoutView, 
    UserProfileView, 
)


router = DefaultRouter()
router.register(r'media-items', MediaItemViewSet)
router.register(r'locais-proximos', LocaisProximosViewSet, basename='locais-proximos')  




urlpatterns = [
    # Rotas de API.
    path('', include(router.urls)),


    # Autenticação
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # Perfil do usuário
    path('profile/', UserProfileView.as_view(), name='profile'),
]
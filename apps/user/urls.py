from django.urls import path
from .views import (
    RegisterView,
    LogoutView,
    UserProfileView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    GoogleLoginView,
)

urlpatterns = [
    # Autenticação tradicional
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Perfil
    path('profile/', UserProfileView.as_view(), name='profile'),

    # Login social
    path('login/google/', GoogleLoginView.as_view(), name='google_login'),
]

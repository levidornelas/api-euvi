from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.media_items.views import MediaItemViewSet
from apps.locais_proximos.views import LocaisProximosViewSet

router = DefaultRouter()
router.register(r'media-items', MediaItemViewSet)
router.register(r'locais-proximos', LocaisProximosViewSet, basename='locais-proximos')

urlpatterns = [
    # Rotas de API
    path('', include(router.urls)),
    
    path('auth/', include('apps.user.urls')),
]
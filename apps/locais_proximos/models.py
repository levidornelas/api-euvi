from django.db import models
from apps.media_items.models import MediaItem

class LocaisProximos(models.Model):
    # Relacionamento com o MediaItem
    media_item = models.ForeignKey(MediaItem, related_name='locais', on_delete=models.CASCADE)
    
    # Nome do local próximo
    name = models.CharField(max_length=255, verbose_name='Nome do Local')
    
    # Descrição do local próximo
    description = models.TextField(verbose_name='Descrição do Local')

    def __str__(self):
        return self.name

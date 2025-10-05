from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.media_items.models import MediaItem
import uuid

class User(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(unique=True, verbose_name='E-mail')
    bio = models.TextField(blank=True, null=True, verbose_name='Biografia')
    avatar = models.URLField(blank=True, null=True, verbose_name='Avatar')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
    
    def __str__(self):
        return f'{self.email} - {self.uuid}'
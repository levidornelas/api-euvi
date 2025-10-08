from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from apps.media_items.models import MediaItem
from .managers import CustomUserManager

class User(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(unique=True, verbose_name='E-mail')
    locais_salvos = models.ManyToManyField(MediaItem, blank=True, related_name='usuarios_que_salvaram')
    bio = models.TextField(blank=True, null=True, verbose_name='Biografia')
    avatar = models.URLField(blank=True, null=True, verbose_name='Avatar')
    
    username = models.CharField(max_length=150, blank=True, null=True, unique=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email.split('@')[0]
                
            base_username = self.username
            counter = 1
            while User.objects.filter(username=self.username).exclude(pk=self.pk).exists():
                self.username = f"{base_username}{counter}"
                counter += 1
            
        super().save(*args, **kwargs)
            

    def __str__(self):
        return f'{self.email} - {self.uuid}'
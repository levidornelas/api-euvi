from django.db import models

class MediaItem(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    latitude = models.FloatField(verbose_name='Latitude')
    longitude = models.FloatField(verbose_name='Longitude')
    media_type = models.CharField(max_length=50, verbose_name='Tipo de Mídia')
    general_info = models.TextField(verbose_name='Informações Gerais')
    opening_hours = models.CharField(max_length=100, blank=True, null=True, verbose_name='Horário de Funcionamento')
    location = models.CharField(max_length=255, verbose_name='Localização')
    maps = models.URLField(max_length=255, blank=True, null=True, verbose_name='Link para Mapas')

    # Autor
    autor = models.CharField(max_length=255, null=True, blank=True, verbose_name='Autor')
    autor_imagem = models.ImageField(upload_to="autores/", null=True, blank=True, verbose_name='Imagem do Autor')
    autor_bio = models.TextField(null=True, blank=True, verbose_name='Biografia do Autor')
    obras = models.TextField(null=True, blank=True, verbose_name='Obras')
    autor_link = models.URLField(null=True, blank=True, verbose_name='Link do Autor')

    # Imagens do Slider
    imagem_cartaz = models.ImageField(upload_to="media/cartazes/", blank=True, null=True, verbose_name='Imagem de Cartaz')
    legenda_1 = models.CharField(max_length=50, null=True, blank=True, verbose_name='Legenda 1')
    imagem_obra = models.ImageField(upload_to="media/obras/", blank=True, null=True, verbose_name='Imagem da Obra')
    legenda_2 = models.CharField(max_length=50, null=True, blank=True, verbose_name='Legenda 2')
    imagem_local = models.ImageField(upload_to="media/locais/", blank=True, null=True, verbose_name='Imagem Local')
    legenda_3 = models.CharField(max_length=50, null=True, blank=True, verbose_name='Legenda 3')

    # Galeria
    outra_imagem1 = models.ImageField(upload_to="media/outras/", blank=True, null=True, verbose_name='Outra Imagem 1')
    outra_imagem2 = models.ImageField(upload_to="media/outras/", blank=True, null=True, verbose_name='Outra Imagem 2')

    def __str__(self):
        return self.title

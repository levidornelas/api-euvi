from django.contrib import admin


from apps.media_items.models import MediaItem 
from apps.locais_proximos.models import LocaisProximos


admin.site.register(LocaisProximos)
admin.site.register(MediaItem)
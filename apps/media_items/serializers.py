from rest_framework import serializers
from .models import MediaItem
from apps.locais_proximos.serializers import LocaisProximosSerializer


class MediaItemSerializer(serializers.ModelSerializer):
    # Adicionando os locais proximos ao serializer de MediaItem
    locais_proximos = LocaisProximosSerializer(many=True, read_only=True)

    class Meta:
        model = MediaItem
        fields = '__all__'

    def create(self, validated_data):
        # Garantir que as imagens sejam URLs válidas
        for field in ['local_image', 'film_image', 'other_image']:
            if field in validated_data and not validated_data[field]:
                validated_data[field] = None  # Define como None se estiver vazio ou inválido

        return MediaItem.objects.create(**validated_data)
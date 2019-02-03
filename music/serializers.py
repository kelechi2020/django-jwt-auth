from rest_framework import serializers

from music.models import Songs


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ('title', 'artist')


class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)
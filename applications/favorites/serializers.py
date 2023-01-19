from rest_framework import serializers


class FavoriteSerializer(serializers.Serializer):
    electronic = serializers.CharField()
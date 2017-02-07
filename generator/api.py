import models
import serializers
from rest_framework import viewsets, permissions


class CharacterViewSet(viewsets.ModelViewSet):
    """ViewSet for the Character class"""

    queryset = models.Character.objects.all()
    serializer_class = serializers.CharacterSerializer
    permission_classes = [permissions.IsAuthenticated]

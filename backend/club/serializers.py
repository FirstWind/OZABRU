from rest_framework import serializers
from .models import SportClub


class SportClubSerializer(serializers.ModelSerializer):
    """Клубы"""
    class Meta:
        model = SportClub
        fields = "__all__"

from rest_framework import serializers
from .models import RegParticipant


class RegParticipantSerializer(serializers.ModelSerializer):
    """регистрация"""

    class Meta:
        model = RegParticipant
        fields = '__all__'

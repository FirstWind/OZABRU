from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import RegParticipant
from .serializers import RegParticipantSerializer


class RegParticipantView(viewsets.ModelViewSet):
    """События"""
    queryset = RegParticipant.objects.all()
    serializer_class = RegParticipantSerializer
    permission_classes = [IsAuthenticated]


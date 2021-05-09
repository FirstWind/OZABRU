from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from backend.club.models import SportClub
from backend.club.serializers import SportClubSerializer


class SportClubView(viewsets.ModelViewSet):
    """Вывод списка событий"""
    queryset = SportClub.objects.all()
    serializer_class = SportClubSerializer
    permission_classes = [IsAuthenticated]


from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Event, ProgramEvent, DisciplineProgram, CrossGroup, RelayRace
from .serializers import EventSerializer, ProgramEventSerializer, DisciplineProgramSerializer, CrossGroupSerializer, \
    RelayRaceSerializer


class EventView(viewsets.ModelViewSet):
    """События"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]


class ProgramEventView(viewsets.ModelViewSet):
    """Программа соревнований"""
    queryset = ProgramEvent.objects.all()
    serializer_class = ProgramEventSerializer
    permission_classes = [IsAuthenticated]


class DisciplineProgramView(viewsets.ModelViewSet):
    """Дисциплины"""
    queryset = DisciplineProgram.objects.all()
    serializer_class = DisciplineProgramSerializer
    permission_classes = [IsAuthenticated]


class CrossGroupView(viewsets.ModelViewSet):
    """Кроссовые"""
    queryset = CrossGroup.objects.all()
    serializer_class = CrossGroupSerializer
    permission_classes = [IsAuthenticated]


class RelayRaceView(viewsets.ModelViewSet):
    """Кроссовые"""
    queryset = RelayRace.objects.all()
    serializer_class = RelayRaceSerializer
    permission_classes = [IsAuthenticated]

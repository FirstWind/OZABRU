from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .license import IsOwnerProfileOrReadOnly
from .models import Location, City, Region, Trainer, Human, KodEvent, Participant, VidSporta, StatusEvent, Referee, \
    Command, Group, UserPhone
from .serializers import LocationSerializer, CitySerializer, RegionSerializer, TrainerSerializer, HumanSerializer, \
    ParticipantSerializer, KodEventSerializer, VidSportaSerializer, StatusEventSerializer, RefereeSerializer, \
    CommandSerializer, GroupSerializer, UserPhoneSerializer


class LocationView(viewsets.ModelViewSet):
    """Вывод списка событий"""
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]


class HumanView(viewsets.ModelViewSet):
    queryset = Human.objects.all()
    serializer_class = HumanSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]


class TrainersView(viewsets.ModelViewSet):
    """список Тренеров"""
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    permission_classes = [IsAuthenticated]


class ParticipantView(viewsets.ModelViewSet):
    """список Участников"""
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = [IsAuthenticated]


class RefereeView(viewsets.ModelViewSet):
    """список Участников"""
    queryset = Referee.objects.all()
    serializer_class = RefereeSerializer
    permission_classes = [IsAuthenticated]


class RegionView(viewsets.ModelViewSet):
    """Вывод списка событий"""
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [IsAuthenticated]


class CityView(viewsets.ModelViewSet):
    """Вывод списка событий"""
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticated]


class KodEventView(viewsets.ModelViewSet):
    queryset = KodEvent.objects.all()
    serializer_class = KodEventSerializer
    permission_classes = [IsAuthenticated]


class VidSportaView(viewsets.ModelViewSet):
    queryset = VidSporta.objects.all()
    serializer_class = VidSportaSerializer
    permission_classes = [IsAuthenticated]


class StatusEventView(viewsets.ModelViewSet):
    queryset = StatusEvent.objects.all()
    serializer_class = StatusEventSerializer
    permission_classes = [IsAuthenticated]


class CommandView(viewsets.ModelViewSet):
    """список Участников"""
    queryset = Command.objects.all()
    serializer_class = CommandSerializer
    permission_classes = [IsAuthenticated]


class GroupView(viewsets.ModelViewSet):
    """список Участников"""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]


class UserPhoneView(viewsets.ModelViewSet):
    """список Участников"""
    queryset = UserPhone.objects.all()
    serializer_class = UserPhoneSerializer
    permission_classes = [IsAuthenticated]

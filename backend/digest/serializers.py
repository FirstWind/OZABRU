from rest_framework import serializers
from .models import Region, City, Location, Human, Trainer, Participant, KodEvent, VidSporta, StatusEvent, Referee, \
    Command, Group, UserPhone


class RegionSerializer(serializers.ModelSerializer):
    """Регионы"""
    class Meta:
        model = Region
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    """Города"""
    class Meta:
        model = City
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    """Локации"""
    class Meta:
        model = Location
        fields = "__all__"


class HumanSerializer(serializers.ModelSerializer):
    """Все зареганные"""
    user_human = serializers.SlugRelatedField(slug_field='email', read_only=True)
    city = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Human
        fields = '__all__'


class TrainerSerializer(serializers.ModelSerializer):
    """Тренера"""
    human = serializers.SlugRelatedField(slug_field='first_name', read_only=True)

    class Meta:
        model = Trainer
        fields = '__all__'


class ParticipantSerializer(serializers.ModelSerializer):
    """Участники"""
    # human = serializers.SlugRelatedField(slug_field='first_name', read_only=True)
    # trainers = serializers.SlugRelatedField(slug_field='email', read_only=True)

    class Meta:
        model = Participant
        fields = '__all__'


class RefereeSerializer(serializers.ModelSerializer):
    """Участники"""
    city = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # human = serializers.SlugRelatedField(slug_field='first_name', read_only=True)
    # status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Referee
        fields = '__all__'


class KodEventSerializer(serializers.ModelSerializer):
    """Дисциплины"""
    # vid_sporta = serializers.SlugRelatedField(slug_field='name', )

    class Meta:
        model = KodEvent
        fields = '__all__'


class VidSportaSerializer(serializers.ModelSerializer):
    """Соревнования"""

    class Meta:
        model = VidSporta
        fields = '__all__'


class StatusEventSerializer(serializers.ModelSerializer):
    """Соревнования"""

    class Meta:
        model = StatusEvent
        fields = '__all__'


class CommandSerializer(serializers.ModelSerializer):
    """Соревнования"""

    class Meta:
        model = Command
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    """Соревнования"""

    class Meta:
        model = Group
        exclude = ('start_year', 'end_year')


class UserPhoneSerializer(serializers.ModelSerializer):
    """Соревнования"""

    class Meta:
        model = UserPhone
        fields = '__all__'
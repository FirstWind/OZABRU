from rest_framework import serializers
from .models import Event, ProgramEvent, DisciplineProgram, CrossGroup, RelayRace


class RelayRaceSerializer(serializers.ModelSerializer):
    """Эстафета"""

    class Meta:
        model = RelayRace
        fields = '__all__'


class CrossGroupSerializer(serializers.ModelSerializer):
    """Кросс дисциплина"""

    class Meta:
        model = CrossGroup
        fields = '__all__'


class DisciplineProgramSerializer(serializers.ModelSerializer):
    """список дисциплин"""
    relayrace_set = RelayRaceSerializer(many=True)
    crossgroup_set = CrossGroupSerializer(many=True)

    class Meta:
        model = DisciplineProgram
        fields = "__all__"


class ProgramEventSerializer(serializers.ModelSerializer):
    """Список событий"""
    # location = serializers.SlugRelatedField(queryset=Location.objects.all(), slug_field='name', read_only=False)
    discipline_program = DisciplineProgramSerializer(many=True)

    class Meta:
        model = ProgramEvent
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    """Список событий"""
    program_event = ProgramEventSerializer(many=True)

    class Meta:
        model = Event
        fields = ['draft', 'vid', 'start_date', 'final_date', 'region', 'name', 'short_description', 'program_event']
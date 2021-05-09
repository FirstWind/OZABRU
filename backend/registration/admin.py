from django.contrib import admin
from related_admin import RelatedFieldAdmin
from .models import RegParticipant


@admin.register(RegParticipant)
class RegParticipantAdmin(RelatedFieldAdmin):
    list_display = ['participant__human__first_name', 'participant__human__last_name', 'participant__human__sex',
                    'participant__category__short_name', 'groups_event',  'get_birth_year']
    # list_filter = ("program__events__name",)
    # inlines = (GroupCross, GroupRelay)

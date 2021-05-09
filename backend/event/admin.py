from django import forms
from django.contrib import admin
from related_admin import RelatedFieldAdmin
from .models import ProgramEvent, Event, DisciplineProgram, RelayRace, CrossGroup
from ckeditor.widgets import CKEditorWidget


class ProgramEventAdminForm(forms.ModelForm):
    program_text = forms.CharField(label="Текст", widget=CKEditorWidget(), required=False)

    class Meta:
        model = ProgramEvent
        fields = '__all__'


# class GroupRelay(admin.TabularInline):
#     model = RelayRace
#
#
# class GroupCross(admin.TabularInline):
#     model = CrossGroup

@admin.register(ProgramEvent)
class ProgramEventAdmin(RelatedFieldAdmin):
    list_display = ["location", "date", "name"]
    form = ProgramEventAdminForm
    list_filter = ('events__region', 'events__start_date', 'events',)


@admin.register(Event)
class EventAdmin(RelatedFieldAdmin):
    list_display = ["name", "start_date", "final_date", "vid__name", "vid__kod", "draft"]
    list_filter = ('region', 'start_date',)
    list_editable = ("draft",)
    actions = ['publish', 'unpublish']

    def unpublish(self, request, queryset):
        """снять с  публикации"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = '1 запись была обновлена'
        else:
            message_bit = f'{row_update} записи были обновлены'
        self.message_user(request, f'{message_bit}')

    def publish(self, request, queryset):
        """поставить на  публикацию"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = '1 запись была обновлена'
        else:
            message_bit = f'{row_update} записи были обновлены'
        self.message_user(request, f'{message_bit}')

    publish.short_description = 'Опубликовать'
    publish.allowed_permissions = ('change',)

    unpublish.short_description = 'Снять с публикации'
    unpublish.allowed_permissions = ('change',)


@admin.register(DisciplineProgram)
class DisciplineProgramAdmin(RelatedFieldAdmin):
    list_display = ["program", "kod_event", "status"]
    list_filter = ("program__events__name",)
    # inlines = (GroupCross, GroupRelay)
    # exclude = ('groups_discipline',)
    # fields = ("event",)

    # def event(self, obj):
    #     return obj.program.events.name


@admin.register(CrossGroup)
class CrossGroupAdmin(admin.ModelAdmin):
    list_display = ["groups", "check_razr", "check_command", "check_ball"]
    list_editable = ("check_razr", "check_command", "check_ball")
    list_filter = ('discipline_program__program__events__name', 'discipline_program__kod_event__name')


@admin.register(RelayRace)
class RelayRaceAdmin(admin.ModelAdmin):
    list_display = ["groups", "limit", "check_razr", "check_command", "check_ball"]
    # list_editable = ("check_razr", "check_command", "check_ball")
    # inlines = [MembershipInline,]
    # list_filter = ('groups_discipline',)


# admin.site.register(GroupsDiscipline, GroupsDisciplineAdmin)


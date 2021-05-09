from django import forms
from django.utils.safestring import mark_safe
from related_admin import RelatedFieldAdmin

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import *

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from ..club.models import SportClub


class UserPhoneInline(admin.TabularInline):
    model = UserPhone
    extra = 0


class TrainerAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget, required=False)

    class Meta:
        model = Trainer
        fields = '__all__'


@admin.register(Trainer)
class TrainerAdmin(RelatedFieldAdmin):
    list_display = ("human", 'vid_sporta', 'human__user_human__email')
    form = TrainerAdminForm
    readonly_fields = ["get_part", 'get_image']

    def get_part(self, obj):
        return [f'{par}' for par in obj.get_participant()]

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.avatar.url} width="60", height="60"')

    get_image.short_description = "Изображение"


@admin.register(Participant)
class ParticipantAdmin(RelatedFieldAdmin):
    list_display = ['human', 'human__user_human__email', 'human__sex', 'human__birthday', 'category', 'date_prisv']
    list_filter = ['vid_sporta__name', 'trainers']
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.avatar.url} width="60", height="60"')

    get_image.short_description = "Изображение"


class CityInline(admin.TabularInline):
    model = City
    extra = 0


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [
        CityInline,
    ]


class LocationInline(admin.TabularInline):
    model = Location
    extra = 0


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["regions__name"]
    inlines = [
        LocationInline,
    ]


# @admin.register(Location)
# class LocationAdmin(admin.ModelAdmin):
#     list_display = ["name"]
#     list_filter = ["cities__regions__name", "cities__name"]


class SportClubInline(admin.TabularInline):
    model = SportClub
    extra = 0


@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    list_display = ['user_human', 'last_name', 'first_name', 'sex', 'birthday']
    list_filter = ['city']
    inlines = [
        UserPhoneInline, SportClubInline
    ]


@admin.register(StatusEvent)
class StatusEventAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Referee)
class RefereeAdmin(admin.ModelAdmin):
    list_display = ["human", "category", "category"]
    list_filter = ["city"]


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ["name_short", "name_long", "sex", "start_year", "end_year"]


@admin.register(Command)
class CommandAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(VidSporta)
class VidSportaAdmin(admin.ModelAdmin):
    list_display = ["name", "kod"]


@admin.register(KodEvent)
class KodEventAdmin(admin.ModelAdmin):
    list_display = ["name", "kod"]
    list_filter = ["vid_sporta__name"]




# @admin.register(UserPhone)
# class UserPhoneAdmin(admin.ModelAdmin):
#     list_display = ["number"]
#     list_filter = ["human"]
#     search_fields = ["human__last_name"]


admin.site.site_header = "O_Zab.ru"


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)

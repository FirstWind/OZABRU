from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from related_admin import RelatedFieldAdmin

from backend.club.models import SportClub


class SportClubAdminForm(forms.ModelForm):
    text = forms.CharField(label="Описание", widget=CKEditorUploadingWidget)


@admin.register(SportClub)
class SportClubAdmin(RelatedFieldAdmin):
    list_display = ('name', 'owner', 'address', 'logo')
    form = SportClubAdminForm
    readonly_fields = ['get_image']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.logo.url} width="60", height="60"')

    get_image.short_description = "Изображение"

    class Meta:
        model = SportClub
        fields = '__all__'
from django.contrib import admin
# from related_admin import RelatedFieldAdmin
from .models import SendTrainer


@admin.register(SendTrainer)
class SendTrainerAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact', 'date', "category"]
    list_filter = ('trainer',)
    exclude = ("date",)
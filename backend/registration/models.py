from datetime import datetime

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from ..digest.models import Participant, Command


class RegParticipant(models.Model):
    """Программа мероприятия"""
    participant = models.ForeignKey(Participant, verbose_name="участник", on_delete=models.CASCADE, related_name="reg_participant")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    groups_event = GenericForeignKey('content_type', 'object_id')
    command = models.ForeignKey(Command, verbose_name="команда", on_delete=models.CASCADE, related_name="comanda")

    def get_birth_age(self):
        return datetime.now().year - self.participant.human.birthday.year

    def get_birth_year(self):
        return self.participant.human.birthday.year


    def __str__(self):
        return self.participant.human.last_name

    class Meta:
        verbose_name = 'Регистрация'
        verbose_name_plural = 'Регистрация'

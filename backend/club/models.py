from django.db import models

from backend.digest.models import VidSporta, Location, Human


class SportClub(models.Model):
    """спортивные клубы"""
    owner = models.ForeignKey(Human, verbose_name="владелец клуба", related_name="club_human", on_delete=models.CASCADE)
    name = models.CharField("Название", max_length=100, unique=True, help_text='Название клуба')
    logo = models.ImageField("Логотип", upload_to="club", blank=True, help_text='Выберите файл до 2Мб')
    address = models.ForeignKey(Location, verbose_name="адрес клуба", related_name="club_address",
                                on_delete=models.CASCADE)
    name_sorev = models.ManyToManyField(VidSporta, verbose_name="Спортивная специализация", related_name='club_sorev')
    participant = models.ManyToManyField(Human, verbose_name="Участники клуба", related_name='participant_club')
    text = models.TextField("О клубе", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клуб'
        verbose_name_plural = 'Клубы'

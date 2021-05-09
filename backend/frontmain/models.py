from django.db import models

from backend.digest.models import Trainer


class SendTrainer(models.Model):
    """связь с тренером"""
    CATEGORY_CHOICES = (
        ('Записаться', 'Записаться к тренеру'),
        ('Спросить', 'Задать вопрос'),
        ('Другое', 'Другое'),
    )
    trainer = models.ForeignKey(Trainer, verbose_name="тренер", related_name='send_trainer', on_delete=models.CASCADE)
    name = models.CharField("Фамилия, Имя", max_length=50, help_text='Фамилия, Имя')
    contact = models.CharField("email или телефон", max_length=15, help_text='email или телефон')
    date = models.DateTimeField("Время создания", auto_now_add=True)
    category = models.CharField("категория", max_length=15, choices=CATEGORY_CHOICES)
    text = models.TextField("Текст", blank=True)

    def __str__(self):
        return self.trainer.human.last_name

    class Meta:
        verbose_name = 'Сообщение тренеру'
        verbose_name_plural = 'Сообщение тренерам'

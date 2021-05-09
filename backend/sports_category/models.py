from django.db import models


class Category(models.Model):
    """разряды"""
    name = models.CharField('разряд', max_length=40, help_text='полное название')
    short_name = models.CharField('разряд', max_length=4, unique=True, help_text='короткое название')
    ball = models.PositiveSmallIntegerField('стоимость разряда')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'разряд'
        verbose_name_plural = 'разряды'

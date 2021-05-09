from phonenumber_field.modelfields import PhoneNumberField

from OZABRU.settings import GENDER_CHOICES

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone

from .managers import CustomUserManager
from ..sports_category.models import Category


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Region(models.Model):
    """список регионов"""  # название край, область...
    name = models.CharField("Название региона", max_length=100, unique=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'


class City(models.Model):
    """список городов(районов)"""  # район области (края), город
    name = models.CharField("Название города(района)", max_length=50, unique=True, blank=True)
    regions = models.ForeignKey(Region, verbose_name="Регион", related_name="city", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город(район)'
        verbose_name_plural = 'Города(районы)'


class Location(models.Model):
    """место проведения"""
    name = models.CharField("место проведения", max_length=100, unique=True, blank=True)
    # metka = models.  В чем хранить геоданные?
    cities = models.ForeignKey(City, verbose_name="Город(район)", related_name="location", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'место проведения'
        verbose_name_plural = 'места проведения'


class Command(models.Model):
    """список команд"""
    name = models.CharField("команда", max_length=50, unique=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'команда'
        verbose_name_plural = 'команды'


class Group(models.Model):
    """список возрастных групп"""
    name_short = models.CharField("возр гр", max_length=10, help_text="короткое название группы", unique=True, blank=True)
    name_long = models.CharField('описание', max_length=70, help_text="полное название группы", unique=True, blank=True)
    sex = models.CharField("Пол", max_length=1, choices=GENDER_CHOICES, blank=True)
    start_year = models.PositiveSmallIntegerField("нач дата", default=0)
    end_year = models.PositiveSmallIntegerField("кон дата", default=0)

    def get_year(self):
        import datetime
        result = datetime.date.today().year - int(self.name_short[-2:]) - 2
        return result

    def save(self, *args, **kwargs):
        self.start_year = self.get_year()
        self.end_year = self.start_year + 2
        super(Group, self).save(*args, **kwargs)

    def __str__(self):
        return self.name_long

    class Meta:
        verbose_name = 'Возрастная группа'
        verbose_name_plural = 'Возрастные группы'


class Human(models.Model):
    """Все люди"""
    city = models.ForeignKey(City, verbose_name="город(регион)", related_name="human", blank=True, null=True,
                             on_delete=models.SET_NULL)
    first_name = models.CharField('Фамилия', max_length=255, blank=True)
    last_name = models.CharField('Имя', max_length=255, blank=True)
    sex = models.CharField("Пол", max_length=1, choices=GENDER_CHOICES, blank=True)
    birthday = models.DateField('Дата рождения', null=True, blank=True)
    user_human = models.OneToOneField(CustomUser, verbose_name="связь с User", related_name="human",
                                      on_delete=models.CASCADE, blank=True, null=True, default=None)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Человека'
        verbose_name_plural = 'Люди'


class VidSporta(models.Model):
    """вид спорта"""  # плавние, ориентирование...

    name = models.CharField("вид спорта", max_length=100, unique=True, blank=True)
    kod = models.CharField("Код", max_length=11, unique=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'вид Спорта'
        verbose_name_plural = 'виды Спорта'


class StatusEvent(models.Model):
    """Статус спортивного события"""
    name = models.CharField("Название", max_length=100, unique=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус события'
        verbose_name_plural = 'Список статусов событий'


class KodEvent(models.Model):
    """Код дисциплины"""
    vid_sporta = models.ForeignKey(VidSporta, verbose_name="вид соревнования", related_name='kod_vid',
                                   on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField("Название", max_length=100, unique=True, blank=True)
    kod = models.CharField("Код", max_length=11, unique=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'вид Дисциплины'
        verbose_name_plural = 'виды дисциплин'


class UserPhone(models.Model):
    """номера телефона у human"""
    human = models.ForeignKey(Human, verbose_name="человек", on_delete=models.CASCADE)
    number = PhoneNumberField("№ Телефона", blank=True, null=True, unique=True)

    def __str__(self):
        return f'{self.human.last_name} {self.human.first_name}'

    class Meta:
        verbose_name = '№ телефона'
        verbose_name_plural = '№ телефонов'


class Referee(models.Model):
    """список судей"""
    CATEGORY_CHOICES = (
        ('ССВК', 'Высшая категория (ССВК)'),
        ('СС1К', 'Первая категория (СС1К)'),
        ('СС2К', 'Вторая категория (СС2К)'),
        ('СС3К', 'Третья категория (СС3К)'),
    )
    STATUS_CHOICES = (
        (1, 'Атестован'),
        (0, 'Не атестован'),
    )
    human = models.OneToOneField(Human, verbose_name="id участникa", on_delete=models.CASCADE, unique=True)
    vid_sporta = models.ForeignKey(VidSporta, verbose_name="вид спорта", related_name="referee_vid_sporta",
                                    on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, verbose_name="город(регион)", on_delete=models.SET_NULL, blank=True, null=True)
    category = models.CharField("категория", max_length=4, choices=CATEGORY_CHOICES, blank=True)
    status = models.BooleanField("статус", choices=STATUS_CHOICES, default=1)

    def __str__(self):
        return f'{self.human.last_name} {self.human.first_name}'

    class Meta:
        verbose_name = 'судья'
        verbose_name_plural = 'судьи'


class Trainer(models.Model):
    """параметры тренера"""
    human = models.OneToOneField(Human, verbose_name="id человека", on_delete=models.CASCADE)
    vid_sporta = models.ForeignKey(VidSporta, verbose_name="вид спорта", related_name="trainer_vid_sporta",
                                    on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField("Описание", blank=True)
    email = models.EmailField("E-mail", null=True, blank=True)
    avatar = models.ImageField("Фото", upload_to="Trainer", blank=True)

    def get_participant(self):
        return self.participant.all()

    # def get_absolute_url(self):
    #     from django.urls import reverse
    #     return reverse("trainer_detail", kwargs={'trainer_detail': trainer.pk})

    def __str__(self):
        return f'{self.human.last_name} {self.human.first_name}'

    class Meta:
        verbose_name = 'тренер'
        verbose_name_plural = 'тренера'


class Participant(models.Model):
    """параметры Участника"""
    human = models.ForeignKey(Human, verbose_name="человек", on_delete=models.CASCADE, related_name="participant_human")
    vid_sporta = models.ForeignKey(VidSporta, verbose_name="вид спорта", related_name="participant_vid_sporta",
                                    on_delete=models.SET_NULL, blank=True, null=True)
    disciplina = models.ForeignKey(KodEvent, verbose_name="дисциплина", related_name="participant_kod_event",
                                   on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name="разряд", related_name="participant_category",
                                 on_delete=models.SET_NULL, blank=True, null=True)
    date_prisv = models.DateField('Дата присвоения', blank=True, null=True)
    # chip = models.CharField("№ чипа", max_length=12, null=True, blank=True, unique=True)
    avatar = models.ImageField("Фото", upload_to="Participant", blank=True)
    trainers = models.ForeignKey(Trainer, verbose_name="id тренера", on_delete=models.SET_NULL, blank=True,
                                 null=True, related_name="participant")

    def __str__(self):
        return self.human.last_name

    class Meta:
        verbose_name = 'участник'
        verbose_name_plural = 'участники'

from datetime import datetime

from django.db import models
from ..digest.models import City, VidSporta, Location, KodEvent, Group, StatusEvent


class Event(models.Model):
    """спорт событие"""
    region = models.ForeignKey(City, verbose_name="Город(район)", on_delete=models.SET_NULL, blank=True, null=True)
    draft = models.BooleanField("Черновик", default=True)  # статус публикации (опубликовано, не опубликовано)
    name = models.CharField("Название", max_length=100, help_text="название события", blank=True)  # Название
    short_description = models.CharField("Текст", max_length=300, blank=True,
                                         help_text="краткое описание (анонс 300симв)")
    start_date = models.DateField("Начало события", default=datetime.today)  # начальная дата
    final_date = models.DateField("Окончание события")  # конечная дата
    vid = models.ForeignKey(VidSporta, verbose_name="Вид события", on_delete=models.CASCADE,
                            help_text="ориентирование,трейл...", blank=True, null=True)
    url = models.URLField('Сторонняя ссылка на событие', null=True, blank=True,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'


class ProgramEvent(models.Model):
    """Программа мероприятия"""
    events = models.ForeignKey(Event, verbose_name="Название мероприятия", related_name="program_event",
                               on_delete=models.CASCADE)
    location = models.ForeignKey(Location, verbose_name="Место(район)", related_name='location',
                                 on_delete=models.SET_NULL, null=True, help_text="локация мероприятия")
    # место проведения
    date = models.DateTimeField("Дата мероприятия")
    name = models.CharField("Название", max_length=80, help_text="судейская, соревнование, экскурсия...", blank=True)
    limit_total = models.PositiveSmallIntegerField("Общий лимит", default=0)  # общий лимит человек
    check_event = models.BooleanField("Соревнование", default=False)
    # идентификатор что событие является соревнованием (checkbox). Если само событие, показываются остальные поля.
    program_doc = models.FileField("Файл информации", upload_to="FileDoc/%Y/%m/%d/", null=True, blank=True)
    program_text = models.TextField("Текст", blank=True)  # тех информация по событию

    def __str__(self):
        return f"{self.name}-{datetime.strftime(self.date, '%d.%m.%Y %H:%m')}"

    class Meta:
        verbose_name = 'Программа'
        verbose_name_plural = 'Программы'
        ordering = ["date"]


class DisciplineProgram(models.Model):
    """список соревновательных дисциплин в программе соревнований"""
    # groups_discipline = models.ManyToManyField(RelayRace, verbose_name="Группы")
    program = models.ForeignKey(ProgramEvent, verbose_name="Программа мероприятия", related_name="discipline_program",
                                on_delete=models.CASCADE)
    kod_event = models.ForeignKey(KodEvent, verbose_name="Код дисциплины",
                                  on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(StatusEvent, verbose_name="Статус", on_delete=models.SET_NULL, null=True,
                               help_text="городские, региональные...")
    event_doc = models.FileField("Положение", upload_to="FileDoc/%Y/%m/%d/", null=True, blank=True,
                                 help_text="загрузить файл")

    def __str__(self):
        return self.program.name

    class Meta:
        verbose_name = 'Дисциплина в мероприятии'
        verbose_name_plural = 'Дисциплины в мероприятии'


class GroupsDiscipline(models.Model):
    """Абстрактная модель возрастных групп"""
    discipline_program = models.ForeignKey(DisciplineProgram, verbose_name="Программа мероприятия",
                                           on_delete=models.CASCADE)
    groups = models.ForeignKey(Group, verbose_name="Группа", on_delete=models.CASCADE)
    check_razr = models.BooleanField("Разряды", default=True)  # Выполнение разрядов (считать или нет) в группу
    check_command = models.BooleanField("Командные очки", default=False)  # командный подсчет(да/нет)
    check_ball = models.BooleanField("Баллы", default=False)  # Считать баллы (да/нет)

    def __str__(self):
        return self.groups.name_short

    class Meta:
        abstract = True


# , limit_choices_to=models.Q(app_label='event', model='disciplineprogram')
class RelayRace(GroupsDiscipline):
    """Возрастные группы для эстафеты (командные)"""
    limit = models.PositiveSmallIntegerField("лимит участников в группе", default=2)

    class Meta:
        verbose_name = 'Группа для эстафеты'
        verbose_name_plural = 'Группы для эстафеты'


class CrossGroup(GroupsDiscipline):
    """Возрастные группы для индивидулаьного"""

    class Meta:
        verbose_name = 'Группа для индивидуальных дисц'
        verbose_name_plural = 'Группы для индивидуальных дисц'

    # Настройка формы регистрации (динамическая таблица) event_reg_view_settings
    # дата открытия регистрации
    # дата закрытия регистрации
    # заявка (количество выбора от сборной, сборной региона, команды, лично)
    # показывать список заявок всем (checkbox)
    # подтверждения участия организатором (checkbox)
    # строгое ограничение участников по возрасту (checkbox)
    # телефон заявителя (checkbox видимость поля)
    # Email заявителя (checkbox видимость поля)
    # выводить полную дату рождения а не только год
    # возраст определяется (исполнится в год соревнования или в след году)
    # выводить телефон каждого участника
    # возможность добавлять новые поля в участнике
    # возможность добавлять новые поля в заявке
    # обязательное заполнение поля примечания
    # подтвердить галочкой наличие обязательных документов(список)
    # таблица регистрации участников
    # id участника
    # id дополнительные параметры участника
    #
    # контакты
    # название (телефон, VK, telegram…)
    # ссылка, номер
    # id соревнования
    #
    # def __str__(self):
    #     return self.name
    #
    # class Meta:
    #     verbose_name = 'Регион'
    #     verbose_name_plural = 'Регионы'

from datetime import datetime

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class CounterBaseModel(models.Model):
    """Базовая модель счетчика электричества."""

    class Meta:
        abstract = True

    A = models.PositiveIntegerField(
        verbose_name='Текущий ток (кол-во Ампер) потребления сети',
        null=False
    )
    kW = models.PositiveIntegerField(
        verbose_name=(
            'Cуммарное потребление энергии (Киловатт) за все время работы'
        ),
        null=False
    )


class Counter(models.Model):
    """Модель счетчика электричества."""

    id = models.PositiveIntegerField(
        primary_key=True,
        unique=True,
        null=False
    )
    port = models.PositiveIntegerField(
        verbose_name='Номер порта на котором размещен счётчик',
        unique=True,
        null=False,
        validators=(
            MinValueValidator(9000, message='Не может быть меньше 9000'),
            MaxValueValidator(65000, message='Не может быть больше 65000')
        )
    )


class CounterValue(CounterBaseModel):
    """Модель для хранения замеров счётчиков электричества."""

    counter = models.ForeignKey(
        Counter,
        on_delete=models.CASCADE,
        related_name='counter_values',
        verbose_name='Показание счётчика',
    )
    timestamp = models.DateTimeField(
        verbose_name='Дата и время снятия показания',
        auto_now_add=True
    )


class SimulateCounter(CounterBaseModel):
    """Исскусственная модель, которая симулирует фактические показатели
    счётчика в данное время."""

    id = models.PositiveIntegerField(
        primary_key=True,
        unique=True,
        null=False
    )

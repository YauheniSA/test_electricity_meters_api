from rest_framework import serializers

from electricity_meters.models import Counter, SimulateCounter, CounterValue


class CounterSerializer(serializers.ModelSerializer):
    """Сериализатор для создания и удаления объектов модели Counter."""

    class Meta:
        model = Counter
        fields = '__all__'


class CounterValueSerializer(serializers.ModelSerializer):
    """Сериализатор для получения последних показаний счетчика по его id."""

    class Meta:
        model = SimulateCounter
        fields = '__all__'


class CounterShortSerializer(serializers.ModelSerializer):
    """Сокращенный сериализатор для выдачи статистики по счётчику."""

    class Meta:
        model = CounterValue
        exclude = ('id', 'counter')

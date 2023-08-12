from rest_framework import mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from electricity_meters.models import Counter, SimulateCounter, CounterValue
from api.serializers import (
    CounterSerializer, CounterValueSerializer, CounterShortSerializer
)


class CreateDeleteViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    pass


class RetrieveViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    pass


class ListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    pass


class CounterViewSet(CreateDeleteViewSet):
    """Вьюсет для создания и удаления объектов модели Counter."""

    queryset = Counter.objects.all()
    serializer_class = CounterSerializer


class CounterDataViewSet(RetrieveViewSet):
    """Вьюсет для получения последних показаний счетчика по его id."""

    queryset = SimulateCounter.objects.all()
    serializer_class = CounterValueSerializer


class CounterDataListViewSet(ListViewSet):
    """Вьюсет для получения статистики по id счетчика и интервалу времени."""

    queryset = CounterValue.objects.all()
    serializer_class = CounterShortSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ('id', 'timestamp')

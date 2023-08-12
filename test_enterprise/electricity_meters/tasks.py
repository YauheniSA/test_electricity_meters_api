from celery import shared_task

from electricity_meters.models import Counter, SimulateCounter, CounterValue


@shared_task
def get_counter_values():
    counters = Counter.objects.all()
    for counter in counters:
        try:
            data = SimulateCounter.objects.get(id=counter.id)
        except Exception:
            continue
        CounterValue.objects.create(
            counter=counter,
            A=data.A,
            kW=data.kW
        )

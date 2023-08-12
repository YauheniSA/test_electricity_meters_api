from django.contrib import admin

from electricity_meters.models import Counter, SimulateCounter, CounterValue


@admin.register(Counter)
class CounterAdmin(admin.ModelAdmin):
    list_display = ('id', 'port')


@admin.register(CounterValue)
class CounterValueAdmin(admin.ModelAdmin):
    list_display = ('counter', 'timestamp', 'A', 'kW')
    list_filter = ('counter', 'A', 'kW')
    search_fields = ('counter', 'timestamp')


@admin.register(SimulateCounter)
class SimulateCounterAdmin(admin.ModelAdmin):
    list_display = ('id', 'A', 'kW')

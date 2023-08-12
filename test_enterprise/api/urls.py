from django.urls import include, path
from rest_framework import routers

from api.views import (
    CounterViewSet, CounterDataViewSet, CounterDataListViewSet
)


app_name = 'api'
router = routers.DefaultRouter()
router.register(r'counter', CounterViewSet, basename='counter')
router.register(
    r'counter-data', CounterDataViewSet, basename='counter_data'
)
router.register(
    r'counter-archive', CounterDataListViewSet, basename='counter_archive'
)


urlpatterns = [path('', include(router.urls))]

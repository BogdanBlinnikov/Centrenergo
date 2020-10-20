import django_filters

from inventory.models import Device


class DeviceCharsFilter(django_filters.FilterSet):
    class Meta:
        model = Device
        fields = ['type', ]

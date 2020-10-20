from django import forms
from django.forms import Form

from inventory.models import Device
from users.models import User


class DeviceCreateForm(Form):
    inv_num = forms.IntegerField(label='Инвентарный номер', required=False)
    user = forms.ChoiceField(label='Пользователь', choices=(User.objects.values_list('id', 'username')))
    # device_type = forms.ChoiceField(label='Тип устройства', choices=(Device.objects.values_list('id', 'type')))
    device_type = forms.CharField(label='Тип устройства', max_length=50, required=False)
    brand_name = forms.CharField(label='Марка', max_length=50, required=False)
    model_name = forms.CharField(label='Модель', max_length=50, required=False)
    diagonal = forms.IntegerField(label='Диагональ', required=False)
    motherboard = forms.CharField(label='Материнская плата', required=False)
    processor = forms.CharField(label='Процессор', max_length=20, required=False)
    clock_frequency = forms.FloatField(label='Частота', required=False)
    ram_type = forms.CharField(label='Тип ОЗУ', max_length=5, required=False)
    ram_size = forms.FloatField(label='Объём ОЗУ', required=False)
    disk_space = forms.CharField(label='Объём диска', required=False)
    windows = forms.CharField(label='Windows', max_length=50, required=False)
    colour = forms.BooleanField(label='Цветной', required=False)
    a3_tray = forms.BooleanField(label='Лоток А3', required=False)

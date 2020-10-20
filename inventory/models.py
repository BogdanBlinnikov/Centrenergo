from django.conf import settings
from django.db import models


class Device(models.Model):
    inv_num = models.IntegerField(null=True, verbose_name='Інвентарний номер')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                             verbose_name='Закріплений за')
    type = models.CharField(max_length=50, null=True, verbose_name='Тип пристрою')

    def __str__(self):
        return self.type+' '+str(self.inv_num)


class DeviceChars(models.Model):
    inv_num = models.ForeignKey(Device, on_delete=models.CASCADE, default=100, related_name='+')
    brand_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Марка')
    model_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Модель')
    diagonal = models.CharField(max_length=50, null=True, blank=True, verbose_name='Діагональ')
    motherboard = models.CharField(max_length=100, null=True, blank=True, verbose_name='Материнська плата')
    processor = models.CharField(max_length=20, null=True, blank=True, verbose_name='Процесор')
    clock_frequency = models.CharField(max_length=50, null=True, blank=True, verbose_name='Частота')
    ram_type = models.CharField(max_length=5, null=True, blank=True, verbose_name='Тип ОЗП')
    ram_size = models.CharField(max_length=50, null=True, blank=True, verbose_name='Об\'єм ОЗП')
    disk_space = models.CharField(max_length=50, null=True, blank=True, verbose_name='Об\'єм диску')
    windows = models.CharField(max_length=50, null=True, blank=True, verbose_name='Windows')
    colour = models.BooleanField(default=False, verbose_name='Кольоровий')
    a3_tray = models.BooleanField(default=False, verbose_name='Лоток А3')

    def __str__(self):
        return str(self.inv_num)

from django.contrib.auth.models import AbstractUser
from django.db import models


class Department(models.Model):
    depart = models.CharField(max_length=100, null=True, verbose_name='Департамент')

    def __str__(self):
        return self.depart


class Division(models.Model):
    depart_div = models.ForeignKey(Department, on_delete=models.SET_NULL,
                                   null=True, blank=True, verbose_name='Департамент')
    div = models.CharField(max_length=100, null=True, verbose_name='Відділ')

    def __str__(self):
        return self.div


class User(AbstractUser):
    patronymic = models.CharField(max_length=50, null=True, verbose_name='По-батькові')
    date_of_birth = models.DateField(null=True, verbose_name='День народження')
    is_dir = models.BooleanField(default=False, verbose_name='Директор')
    department_user = models.ForeignKey(Department, on_delete=models.SET_NULL,
                                        null=True, blank=True, verbose_name='Департамент')
    division_user = models.ForeignKey(Division, on_delete=models.SET_NULL,
                                      null=True, blank=True, verbose_name='Відділ')
    position = models.CharField(max_length=100, null=True, verbose_name='Посада')
    tel_number = models.CharField(max_length=14, null=True, verbose_name='Тел. номер')
    short_tel_number = models.CharField(max_length=5, null=True, verbose_name='Короткий тел. номер')

    def __str__(self):
        return self.last_name + ' ' + self.first_name

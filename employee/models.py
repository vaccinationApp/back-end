# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class EmployeeType(models.Model):
    name = models.CharField(max_length=100,verbose_name='Тип работника')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип работника'
        verbose_name_plural = 'Типы работников'


class Department(models.Model):
    name = models.CharField(max_length=100,verbose_name = 'Название Отдела')
    address = models.CharField(max_length=100,verbose_name ='Адрес')
    coordinate = models.CharField(blank=True,null=True,max_length=1000,verbose_name = 'Координаты' , help_text="Координаты отдела(можно найти через google maps) Выглядит так 43.202556, 76.632247")
    region = models.ForeignKey('farmer.Region',on_delete=models.CASCADE,verbose_name = "Район")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

class Employee(models.Model):
    id = models.CharField(max_length=20,primary_key=True,verbose_name = "ИИН работника")
    employeeskey = models.CharField(max_length=1000,verbose_name = 'Пароль')
    name = models.CharField(max_length=100,verbose_name = "ФИО")
    employeetype = models.ForeignKey(EmployeeType,on_delete=models.CASCADE,verbose_name = "Тип работника")
    department = models.ForeignKey(Department,on_delete=models.CASCADE,verbose_name = "Отдел")
    ruraldistrict = models.ForeignKey('farmer.RuralDistrict', on_delete=models.CASCADE, verbose_name='Сельский округ')
    phone = models.CharField(max_length=30,verbose_name='Номер телефона')


    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
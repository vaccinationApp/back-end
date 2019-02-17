# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models






class Disease(models.Model):
    name = models.CharField(max_length=100,verbose_name = 'Болезнь',help_text="название болезни")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Болезнь'
        verbose_name_plural = 'Болезни'

class Modeofapplication(models.Model):
    name = models.CharField(max_length=100, verbose_name = 'Способ ввода',help_text="Способ применения(внутримышечно....)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ввод препарата'
        verbose_name_plural = 'Способы ввода препарата'


class Medicine(models.Model):
    id = models.CharField(max_length=100,primary_key=True,verbose_name='Номер вакцины')
    name = models.CharField(max_length=100,verbose_name = 'Вакцина',help_text="название лекарства(если есть одино лекарство,но объем(мл) разный,то нужно вводить каждый)")
    volume = models.IntegerField(verbose_name='Объем', help_text='миллилитры(мл)')
    dose = models.IntegerField(verbose_name = 'Доза',help_text="количество доз на каждый флакон")
    disease = models.ForeignKey(Disease,on_delete=models.CASCADE,verbose_name = 'Болезнь',help_text="Название болезней,которые лечит это лекарство")
    modeofapplication = models.ForeignKey(Modeofapplication,on_delete=models.CASCADE,verbose_name = 'Способ ввода',help_text="Способ применения(внутримышечно....)")
    typesoflivestock = models.ForeignKey('livestock.TypesofLiveStock', on_delete=models.CASCADE,verbose_name = 'Тип животного' ,help_text="тип животного(у каждого разная доза)")
    description = models.CharField(max_length=1000,verbose_name = 'Описание',help_text="Описание лекарства(Пропорции на вес,когда лучше ставить,с чем нельзя ставить и т.д)Заметка для вакцинатора")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вакцина'
        verbose_name_plural = 'Вакцины'


class Vaccination(models.Model):
    employee = models.ForeignKey('employee.Employee', on_delete=models.CASCADE,verbose_name = 'Вакцинатор',help_text="Вакцинатор")
    livestock = models.ForeignKey('livestock.LiveStock', on_delete=models.CASCADE,verbose_name = 'Животное',help_text="Номер животного")
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE,verbose_name = 'Вакцина',help_text="Лекарство")
    date = models.DateField(verbose_name = 'Дата',help_text="Время, когда поставили вакцину")
    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Вакцинация'
        verbose_name_plural = 'Вакцинации'


class TestMethod(models.Model):
    name = models.CharField(max_length=100,verbose_name='Вид исследования')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Вид Исследования'
        verbose_name_plural='Виды Исследований'

class Bloodtest(models.Model):
    id = models.CharField(max_length=100,primary_key=True,verbose_name='Номер теста')
    livestock = models.ForeignKey('livestock.LiveStock', on_delete=models.CASCADE, verbose_name='Животное',help_text="Номер животного")
    employee = models.ForeignKey('employee.Employee', on_delete=models.CASCADE,verbose_name = 'Вакцинатор')
    disease = models.ForeignKey(Disease,on_delete=models.CASCADE,verbose_name = 'Болезнь',null=True,blank=True,)
    testmethod = models.ForeignKey(TestMethod,on_delete=models.CASCADE,verbose_name='Вид исследования',null=True,blank=True,)
    status = models.BooleanField(verbose_name = 'Статус',help_text="Положительный/Отрицательный",null=True,blank=True,)
    date = models.DateField(verbose_name = 'Дата')

    def __str__(self):
        return self.id


    class Meta:
        verbose_name = 'Тест крови'
        verbose_name_plural = 'Тесты крови'
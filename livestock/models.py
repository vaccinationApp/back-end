# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models

class Sex(models.Model):
    name = models.CharField(max_length=20,verbose_name = 'Пол')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Полы'



class Suit(models.Model):
    name = models.CharField(max_length=100,verbose_name = 'Масть животного/Порода')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Масть'
        verbose_name_plural = 'Масти'

class TypesofLiveStock(models.Model):
    name = models.CharField(max_length=100,verbose_name = 'Вид животного',help_text="вид скота(крупнорогатый,лошади,верблюды)")
    suit = models.ForeignKey(Suit,on_delete=models.CASCADE,verbose_name = 'Масть животного')

    def __str__(self):
        return self.name+"|"+str(self.suit)

    class Meta:
        verbose_name = 'Вид животного'
        verbose_name_plural = 'Виды животных'


class LiveStock(models.Model):
    id = models.CharField(max_length=100,primary_key=True,verbose_name = 'Номер животного',help_text='KZB212345678')
    sex = models.ForeignKey(Sex,on_delete=models.CASCADE,verbose_name = 'Пол животного')
    age = models.IntegerField(verbose_name = 'Месяцы')
    typeoflivestock = models.ForeignKey(TypesofLiveStock, on_delete=models.CASCADE, verbose_name = 'Тип Животного')
    farmer = models.ForeignKey('farmer.Farmer',on_delete=models.CASCADE,verbose_name = 'ИИН Владельца животного')
    placeofbirth = models.ForeignKey('farmer.Village',on_delete=models.CASCADE,verbose_name = 'Населенный пункт',help_text="Поселок,где родилось животное")
    def __str__(self):
        return self.id


    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name="имя")

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='Укажите название')
    price = models.FloatField(max_length=100, verbose_name='Укажите цену')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


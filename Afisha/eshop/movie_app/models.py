from django.db import models
from django.utils.version import version_component_re


class Director(models.Model):
    name = models.CharField(max_length=50, verbose_name='Укажите имя режисера')

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=50, verbose_name='Укажите название фильма')
    description = models.TextField(verbose_name='Укажите описание фильма', default='Lorem ipsum')
    duration = models.FloatField(verbose_name='Укажите продолжительность')
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}--{self.duration}'

class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.movie}--{self.text}'

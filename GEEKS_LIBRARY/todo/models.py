from django.db import models
from main_page.models import Library

class Order(models.Model):
    name = models.CharField(max_length=100, verbose_name='Укажите имя заказчика')
    phone_number = models.IntegerField(verbose_name='Укажите номер телефона заказчика')
    book = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='orders', verbose_name='Укажите книгу')

    def __str__(self):
        return f'{self.name}-{self.book}'

from django.db import models

class Device(models.Model):
    CATEGORY_CHOICES = (
        ('Смартфон', 'Смартфон'),
        ('Планшет', 'Планшет'),
        ('Умные часы', 'Умные часы')
    )
    title = models.CharField(max_length=100, verbose_name='Укажите название устройства')
    manufacturer = models.CharField(max_length=100, verbose_name='Укажите производителя')
    price = models.FloatField(verbose_name='Укажите цену')
    start_device = models.DateField(verbose_name='Укажите дату выхода')
    image = models.ImageField(upload_to='images/', verbose_name='Загрузите фото')
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Смартфон', verbose_name='Укажите категорию')
    feature = models.CharField(max_length=100, verbose_name='Укажите особенности')

    class Meta:
        verbose_name = 'Девайс'
        verbose_name_plural = 'Девайсы'

    def __str__(self):
        return f'{self.title}-{self.price}'

class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name="имя")

    def __str__(self):
        return self.name

class Model(models.Model):
    title = models.CharField(max_length=50, verbose_name='Укажите модель')
    price = models.FloatField(max_length=100, verbose_name='Укажите цену')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
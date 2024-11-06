from django.db import models

class Library(models.Model):
    GENRE_CHOICES = (
        ('Детектив', 'Детектив'),
        ('Любовный роман', 'Любовный роман'),
        ('Фантастика', 'Фантастика'),
        ('Мистика', 'Мистика'),
        ('Исторический роман', 'Исторический роман'),
        ('Авантюрный', 'Авантюрный')
    )
    image = models.ImageField(upload_to='images/', verbose_name='Загрузите фото')
    title = models.CharField(max_length=100, verbose_name='Укажите название книги')
    description = models.TextField(verbose_name='Укажите описание книги', default='Lorem ipsum')
    price = models.FloatField(verbose_name='Укажите цену')
    start_book = models.DateField(verbose_name='Укажите дату выхода')
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES, default='Фантастика',
                             verbose_name='Укажите жанр')
    gmail = models.EmailField(verbose_name='Укажите почту автора')
    author = models.CharField(max_length=40, verbose_name='Укажите автора')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
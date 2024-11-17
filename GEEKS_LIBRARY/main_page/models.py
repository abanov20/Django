from django.core.validators import MinValueValidator, MaxValueValidator
from tkinter.constants import CASCADE

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
    author = models.CharField(max_length=40, verbose_name='Укажите автора',
                              validators=[MinValueValidator(1), MaxValueValidator(5)])

    def average_rating(self):
        reviews = self.review_book.all()
        if reviews:
            return sum(review.mark for review in reviews) / reviews.count()
        return None


    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'{self.title}-{self.price}'

class ReviewBook(models.Model):
    review_book = models.ForeignKey(Library, on_delete=models.CASCADE,
                                    related_name='review_book')
    created_at = models.DateField(auto_now_add=True)
    description = models.TextField(verbose_name='Оставьте отзв о книге')
    mark = models.PositiveIntegerField(verbose_name='Укажите отзыв от 1 до 5')

    class Meta:
        verbose_name = 'Каментарий'
        verbose_name_plural = 'Каментарии'
    def __str__(self):
        return f'{self.review_book}-{self.created_at}'
# Generated by Django 5.1.2 on 2024-11-12 13:36

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='library',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterField(
            model_name='library',
            name='author',
            field=models.CharField(max_length=40, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Укажите автора'),
        ),
        migrations.AlterField(
            model_name='library',
            name='genre',
            field=models.CharField(choices=[('Детектив', 'Детектив'), ('Любовный роман', 'Любовный роман'), ('Фантастика', 'Фантастика'), ('Мистика', 'Мистика'), ('Исторический роман', 'Исторический роман'), ('Авантюрный', 'Авантюрный')], default='Фантастика', max_length=100, verbose_name='Укажите жанр'),
        ),
        migrations.CreateModel(
            name='ReviewBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('description', models.TextField(verbose_name='Оставьте отзв о книге')),
                ('mark', models.PositiveIntegerField(verbose_name='Укажите отзыв от 1 до 5')),
                ('review_film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_book', to='main_page.library')),
            ],
            options={
                'verbose_name': 'Каментарий',
                'verbose_name_plural': 'Каментарии',
            },
        ),
    ]

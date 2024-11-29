# Generated by Django 5.1.3 on 2024-11-29 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Device",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=100, verbose_name="Укажите название устройства"
                    ),
                ),
                (
                    "manufacturer",
                    models.CharField(
                        max_length=100, verbose_name="Укажите производителя"
                    ),
                ),
                ("price", models.FloatField(verbose_name="Укажите цену")),
                ("start_device", models.DateField(verbose_name="Укажите дату выхода")),
                (
                    "image",
                    models.ImageField(
                        upload_to="images/", verbose_name="Загрузите фото"
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Смартфон", "Смартфон"),
                            ("Планшет", "Планшет"),
                            ("Умные часы", "Умные часы"),
                        ],
                        default="Смартфон",
                        max_length=100,
                        verbose_name="Укажите категорию",
                    ),
                ),
                (
                    "feature",
                    models.CharField(
                        max_length=100, verbose_name="Укажите особенности"
                    ),
                ),
            ],
            options={
                "verbose_name": "Девайс",
                "verbose_name_plural": "Девайсы",
            },
        ),
    ]
# Generated by Django 5.1.2 on 2024-11-12 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_alter_library_options_alter_library_author_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewbook',
            old_name='review_film',
            new_name='review_book',
        ),
    ]

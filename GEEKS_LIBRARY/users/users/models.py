from django.db import models
from django .contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(User):
    QUALIFICATIONS = [
        ('J', 'Junior'),
        ('M', 'Middle'),
        ('S', 'Senior')
    ]
    surname = models.CharField(max_length=50)
    qualifications = models.CharField(max_length=20, choices=QUALIFICATIONS, default='J')

    def save(self, *args, **kwargs):
        qualifications = self.qualifications

        if qualifications == 'J':
            self.qualifications = 'Junior-300$'
        elif qualifications == 'M':
            self.qualifications = 'Middle-1000$'
        elif qualifications == 'S':
            self.qualifications = 'Senior-2000$'
        else:
            self.qualifications = 'у вас нет квалификации'

        super().save(*args, **kwargs)
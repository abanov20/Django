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

@receiver(post_save, sender=CustomUser)
def set_user(sender, instance, created, **kwargs):
    print('Сигнал успешно обработан пользователь создан')
    qualifications = instance.qualifications
    if qualifications == 'Junior':
        instance.qualifications = 'Junior-300$'
    elif qualifications == 'Middle':
        instance.qualifications = 'Middle-1000$'
    elif qualifications == 'Senior':
        instance.qualifications = 'Senior-2000$'
    else:
       instance.qualifications = 'у вас нет квалификации'
    instance.save()


from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.db.models.signals import post_save
from django.dispatch import receiver

QUALIFICATIONS = [
    ('J', 'Junior'),
    ('M', 'Middle'),
    ('S', 'Senior')
]

class CustomRegistrationForm(UserCreationForm):
    password = forms.CharField(required=True)
    user_name = forms.CharField(required=True)
    name = forms.CharField(required=True)
    surname = forms.CharField(required=True)
    qualifications = forms.ChoiceField(required=True, choices=QUALIFICATIONS)

    class Meta:
        model = models.CustomUser
        fields = (
            "username",
            "password",
            "name",
            "surname",
            "qualifications",
        )

    def save(self, commit=True):
        user = super(CustomRegistrationForm, self).save(commit=True)
        user.password = self.cleaned_data["password"]
        if commit:
            user.save()
        return user

@receiver(post_save, sender=models.CustomUser)
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

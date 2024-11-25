from django import forms
from . import models, parser_labirint
from .models import labirint


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('labirint', 'labirint'),
    )

    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]
    def parser_data(self):
        if self.data['media_type'] == 'labirint':
            labirint_pars = parser_labirint.parsing()
            for i in labirint_pars:
                models.labirint.objects.create(**i)
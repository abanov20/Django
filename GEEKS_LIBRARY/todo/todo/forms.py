from django import forms
from . import models

class ToDoForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = "__all__"
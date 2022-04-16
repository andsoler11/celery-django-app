from django import forms
from django.forms import ModelForm
from .models import Menu


class DateInput(forms.DateInput):
    input_type = 'date'


class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = ['title', 'menu_day']

        label = {
            'title': 'add title to the menu',
            'menu_day': "menu's day"
        }

        widgets = {
            'menu_day': DateInput(),
        }
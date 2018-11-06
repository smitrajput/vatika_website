from django import forms

from .models import Menu


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('item_name', 'item_price')
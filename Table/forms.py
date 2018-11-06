from django import forms

from .models import BookTable


class BookTableForm(forms.ModelForm):
    
    class Meta:
        model = BookTable
        fields = ('customer', 'contact','email','total_persons','date','time')
        widgets = {
            'date': forms.DateInput(attrs={'class':'datepicker'}),
        }

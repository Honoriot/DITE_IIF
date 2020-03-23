from django import forms
from .models import FORM


class form_detail(forms.ModelForm):
    class Meta:
        model = FORM
        fields = [
            'Name',
            'Email',
            'Phone_No',
            'College_Name',
            'Suggestions',
            'Featured'
        ]


class Raw_form(forms.Form):
    Name = forms.CharField(help_text='User Name', max_length=15)
    Email = forms.EmailField(max_length=256)
    Phone_No = forms.IntegerField()
    College_Name = forms.CharField(widget=forms.Textarea)
    Suggestions = forms.CharField(widget=forms.Textarea,help_text="Improvement is important..")
    Featured = forms.BooleanField()        
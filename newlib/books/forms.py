from django import forms
from django.core.exceptions import ValidationError

from .models import Books

class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ('title','text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={"class": "form-control mb5"})
        }
        labels = {
            'text': 'Write your thoughts here:'
        }

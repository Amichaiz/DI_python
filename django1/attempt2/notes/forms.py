from django import forms
from django.core.exceptions import ValidationError
from .models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets = {
            'text': forms.Textarea(attrs={"class": "form-control nm-5"}),
            'title': forms.TextInput(attrs={"class": "form-control nm-5"})
        }
        labels = {
            'text': 'write thoughts here'
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError('We only except notes about Jango')
        return title

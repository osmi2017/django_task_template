from django import forms
from .models import Contact_request


class AddForm(forms.ModelForm):

    class Meta:
        model = Contact_request
        fields = ('email', 'name', 'content', 'date')

        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.TextInput(attrs={'class': 'form-control'}),
        }
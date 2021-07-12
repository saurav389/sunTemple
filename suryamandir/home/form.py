from django import forms
from .models import contactus

class contactForm(forms.ModelForm):
    class Meta:
        model = contactus
        fields = [
            'Name',
            'Email',
            'Number',
            'Query',
          
        ]
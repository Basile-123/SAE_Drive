from django.forms import ModelForm
from django import forms
from .models import Commande, LigneProduit

class CommandeForm(ModelForm):
    class Meta:
        model = Commande
        fields = ['client', 'date']
        widgets = {
            'client': forms.Select(),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class LigneProduitForm(ModelForm):
    class Meta:
        model = LigneProduit
        fields = ['commande', 'produit', 'quantite']
        widgets = {
            'commande': forms.Select(),
            'produit': forms.Select(),
            'quantite': forms.NumberInput(attrs={'min': '1'}),
        }
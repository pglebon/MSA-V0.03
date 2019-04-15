from django import forms

from .models import Partenaire

class PartenaireForm(forms.ModelForm):
     class Meta:
        model = Partenaire
        fields =  '__all__'

class PartFilterForm(forms.Form):
        nom = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Nom'}),)
        prenom = forms.CharField(required=False,  widget=forms.TextInput(attrs={'placeholder': 'Prénom'}),)
        tel = forms.CharField(required=False,  widget=forms.TextInput(attrs={'placeholder': 'Tel'}),)
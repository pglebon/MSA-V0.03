from django import forms

from .models import Vehicule, Categorie
from .models import Marque

class PostForm(forms.ModelForm):
     class Meta:
        model = Vehicule
        fields = [   # '__all__'
            'categorie',
            'Immatriculation',
            'Marque',
            'Description',
            'DatePMEC',
            'Couleur',
            'NBPortes',
            'NbCles',
            'DispoVente',
            'DispoLocation',
            'Archive', ]
        #widgets = {
        #    'Description': Textarea(attrs={'cols': 80, 'rows': 3}),
        #}

class formCategorie(forms.ModelForm):
     class Meta:
        model = Categorie
        fields =  '__all__' 
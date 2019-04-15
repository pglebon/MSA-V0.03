from django import forms
#from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget

from .models import Reservation

class dateForm(forms.Form):
    date_debut = forms.DateField( 
        label = 'Date de début', 
        widget=AdminDateWidget(),)
    heure_debut = forms.TimeField(
        label = '',
        widget=AdminTimeWidget(),)
    date_fin = forms.DateField( 
        label = 'Date de fin', 
        widget=AdminDateWidget(),)
    heure_fin = forms.TimeField(
        label = '',
        widget=AdminTimeWidget(),)

class FormRechPartenaire(forms.Form):
    nom = forms.CharField(label='Nom', max_length=100,empty_value=True)
    
class FormReservation(forms.ModelForm):
     class Meta:
        model = Reservation
        fields =  '__all__'

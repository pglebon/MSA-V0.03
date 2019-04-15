from django.db import models
from django.db.models import Q
from django.core.exceptions import ValidationError 

from vehicule.models import Vehicule
from partenaire.models import Partenaire


# Create your models here.
class Reservation(models.Model):
    vehicule = models.ForeignKey(
                Vehicule,
                on_delete=models.CASCADE,
                related_name="Vehicule")
    client = models.ForeignKey(
                Partenaire,
                on_delete=models.CASCADE,
                related_name="Client")
    conducteur1 = models.ForeignKey(
                Partenaire,
                on_delete=models.CASCADE,
                related_name="conducteur1")
    conducteur2 = models.ForeignKey(
                Partenaire,
                on_delete=models.CASCADE,
                related_name="conducteur2",null=True, blank=True)
    debut = models.DateTimeField( )
    Fin = models.DateTimeField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    create_by = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        retour = self.vehicule.pk + " du " + self.debut.strftime("%d-%m-%Y") + " au " + self.Fin.strftime("%d-%m-%Y")
        return "%s" % (retour) 

    def save(self, *args, **kwargs):
        if self.debut > self.Fin :  raise ValidationError('Date de début > date fin')

        if self.pk is None:
            if Reservation.objects.filter(
                      Q(vehicule=self.vehicule),
                      ~ (Q(debut__gt=self.debut) & Q(debut__gt=self.Fin)|
                      Q(Fin__lt=self.debut) & Q(Fin__lt=self.Fin))):
                raise ValidationError('Véhicule non dispo.')
        else :
            test = Reservation.objects.filter(
                      ~Q(pk=self.pk),
                      Q(vehicule=self.vehicule),
                      ~ (Q(debut__gt=self.debut) & Q(debut__gt=self.Fin)|
                      Q(Fin__lt=self.debut) & Q(Fin__lt=self.Fin)))

            if test:    raise ValidationError('Véhicule non dispo.')        
        super().save(*args, **kwargs)    
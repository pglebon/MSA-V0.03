from django.db import models
from django.template.defaultfilters import truncatewords

# Create your models here.
class Marque(models.Model):
    Marque = models.CharField(max_length=20 , primary_key=True)
    Favoris = models.IntegerField(null = True)
    LogoUrl = models.FileField(upload_to='logo/',null = True)
    def __str__(self):
        return "%s" % (self.Marque)

class Categorie(models.Model):
    categorie = models.CharField(max_length=1, primary_key=True)
    tarif = models.DecimalField(max_digits=15, decimal_places=3)
    description = models.TextField()
    def __str__(self):
        return "%s" % (self.categorie )#+ " " + str(self.Tarif) + "€/jrs " + truncatewords(self.Description, 10))

class Vehicule(models.Model):
    Immatriculation = models.CharField(max_length=20, primary_key=True)
    Marque =  models.ForeignKey('Marque', on_delete=models.CASCADE,)
    Description = models.TextField()
    DatePMEC = models.DateField()
    Couleur = models.CharField(max_length=20, null=True,blank=True)
    NBPortes = models.IntegerField( null = True ) 
    NbCles = models.IntegerField(null = True)
    DispoVente = models.BooleanField(default=False)
    DispoLocation = models.BooleanField(default=False)
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, null=True, blank=True,)
    Archive = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    create_by = models.CharField(max_length=20, null=True, blank=True)
    def __str__(self):
        return "%s" % (self.Immatriculation)
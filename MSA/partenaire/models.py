from django.db import models

# Create your models here.
class Partenaire(models.Model):
    type_titre = (
        ('1', 'Madame'),
        ('2', 'Monsieur'),
        ('3', 'Société'),
    )
    Titre = models.CharField(max_length=1, choices=type_titre, default='2',blank=True)
    RaisonSociale = models.CharField(max_length=50, null=True,blank=True)
    Nom = models.CharField(max_length=50,)
    Prenom = models.CharField(max_length=150)
    Adresse = models.TextField( null=True,blank=True)
    Telephone = models.CharField(max_length=20, null=True, blank=True)
    Email = models.EmailField(max_length=200, null=True, blank=True)
    DateNaissance = models.DateField( null=True , blank=True)
    NumeroPermis = models.CharField(max_length=50, null=True, blank=True)
    DatePermis = models.DateField( null=True , blank=True)
    VillePermis = models.CharField(max_length=30, null=True, blank=True)
    DateCreation = models.DateTimeField('Date de création', null=True, blank=True)
    def __str__(self):
        retour = self.Nom + " - " + self.Prenom
        if self.RaisonSociale is not None :
            retour = self.RaisonSociale + " ( " + retour + " ) " 
        return "%s" % (retour) 
    def save(self):
       self.Nom = self.Nom.upper()
       if self.RaisonSociale is not None : 
           self.RaisonSociale = self.RaisonSociale.upper()
       super(Partenaire, self).save()
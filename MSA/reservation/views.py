from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, HttpResponseRedirect
from django.core import serializers
from datetime import date, datetime, timedelta
from reservation.utils.calcules import CalendrierResa
import calendar
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from vehicule.models import Vehicule
from vehicule.models import Categorie
from partenaire.models import Partenaire
from .models import Reservation
from .forms import dateForm, FormRechPartenaire, FormReservation
 	

class resa_calend:

    def __init__(self, date, vehicule):
        """Constructeur de notre classe"""
        self.date = date
        self.vehicule = vehicule



@login_required(login_url='/accounts/login/')
def index(request):


    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        resa = FormReservation()
        # create a form instance and populate it with data from the request:
        form = dateForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            DateDebut = str(form.cleaned_data['date_debut'])
            HeureDebut = str(form.cleaned_data['heure_debut'])
            DateFin = str(form.cleaned_data['date_fin'])
            HeureFin = str(form.cleaned_data['heure_fin'])

            #Calcule du nombre de jours
            date_delta = form.cleaned_data['date_fin'] - form.cleaned_data['date_debut']

            str_debut = DateDebut  + " " + HeureDebut
            str_Fin = DateFin + " " + HeureFin

            #resa.fields["debut"].initial = datetime.strptime(str_debut, "%Y-%m-%d %H:%M:%S")
            #resa.fields["Fin"].initial = datetime.strptime(str_Fin, "%Y-%m-%d %H:%M:%S")
            
            request.session["date_resa"] = form.data 
            request.session["debut"] = str_debut 
            request.session["fin"] = str_Fin
            request.session["nbjours"] = date_delta.days + 1

            return HttpResponseRedirect('categorie/')

        # if a GET (or any other method) we'll create a blank form
    else:
       form = dateForm()

    titre = 'Réservation'
    context = {
        'form': form,
        'Titre': titre ,
    }
    return render(request, 'reservation/index.html', context )


@login_required(login_url='/accounts/login/')
def ListeReservation(request):
    liste_vehicule = Vehicule.objects.order_by('Immatriculation')
    liste_resa = Reservation.objects.order_by('vehicule')

    calendrierResa = CalendrierResa(datetime.now(),60)

    if 'listResa' in locals(): listResa.clear()
    listResa = [[]]

    cpt = 0
    for vehicule in liste_vehicule :
      cpt = cpt + 1 
      listResa.append([])
      oldCollsAttribut = {'resa':vehicule.pk,'color':'white','link':' ','first':'X','span':'1'}
      listResa[cpt].append(oldCollsAttribut)
      cptSpan = 0
      for mydate in calendrierResa.allDays :

          for resa in liste_resa :
            if resa.vehicule != vehicule: continue

            if resa.debut.strftime("%Y%m%d") <= datetime.strptime(mydate,"%Y%m%d").strftime("%Y%m%d") <= resa.Fin.strftime("%Y%m%d"):
                CollsAttribut = {'resa':resa,'color':'gray','link':'X', 'first':' ','span':''}
                break
            else:
                CollsAttribut = {'resa':'','color':'white','link':' ','first':' ','span':''}

          if oldCollsAttribut['first'] == 'X' :
              oldCollsAttribut = dict(CollsAttribut)
          if oldCollsAttribut != CollsAttribut:
               oldCollsAttribut.update({'span':cptSpan})
               listResa[cpt].append(oldCollsAttribut)  
               cptSpan = 0
               oldCollsAttribut = dict(CollsAttribut)

          cptSpan = cptSpan + 1

      oldCollsAttribut.update({'span':cptSpan})
      listResa[cpt].append(oldCollsAttribut)            

    titre = 'Réservations'
    context = {
        'Titre': titre ,
        'nbDaysInMonth' : calendrierResa.nbDaysMonth,
        'allDates' : calendrierResa.allDays2,
		'listResa' : listResa, 
    } 
    return render(request,'reservation/listeResa.html', context)


@login_required(login_url='/accounts/login/')
def choixCategorie(request):

    liste_categories = Categorie.objects.order_by('categorie')
    titre = 'Choix de la categorie de véhicule'

    prix_loc = {}
    for categorie in liste_categories :
        prix_loc[categorie.pk]  = categorie.tarif * request.session.get('nbjours')


    context = {
        'Titre': titre ,
        'date_resa': request.session.get('date_resa'),
        'nbjours': request.session.get('nbjours'),
        'liste_categories': liste_categories ,
        'prix_loc': prix_loc
    }
    return render(request,'reservation/categorie.html', context)


@login_required(login_url='/accounts/login/')
def choixVehicule(request,categorie):
    titre = 'Choix du véhicule'

    categ = Categorie.objects.filter(pk=categorie)
    total_tarif =  categ[0].tarif * request.session.get('nbjours')
    txt_categorie = "Catégorie : {} - {}/€jours - total {} €".format( categ[0].categorie, categ[0].tarif, total_tarif) 


    debut = datetime.strptime(request.session.get('debut'), "%Y-%m-%d %H:%M:%S")
    Fin = datetime.strptime(request.session.get('fin'), "%Y-%m-%d %H:%M:%S")


    # Liste des véhicules déja réservé pandant la période
    liste_res    = Reservation.objects.filter(
                  ~(Q(debut__gt=debut) & Q(debut__gt=Fin)|
                  Q(Fin__lt=debut) & Q(Fin__lt=Fin))).values("vehicule") 

    #Liste des véhicules de la catégorie non réservé
    liste_vehicules =  Vehicule.objects.filter(
                 Q(categorie = categorie),
                 Q(DispoLocation = True),
                 ~Q(Immatriculation__in=liste_res))

    context = {
        'Titre': titre ,
        'date_resa': request.session.get('date_resa'),
        'nbjours': request.session.get('nbjours'),
        'categorie' : txt_categorie,
        'liste_vehicules': liste_vehicules
    }
    request.session['categorie'] =  categorie 
    request.session['txt_categorie'] = txt_categorie
    return render(request,'reservation/choixVehicule.html', context)


@login_required(login_url='/accounts/login/')
def choixClient(request,immatriculation):
    titre = 'Choix du client'
    vehicule = get_object_or_404(Vehicule, pk=immatriculation)
    liste_client = Partenaire.objects.filter(Nom= '*')

    if request.method == 'POST':
        RechPart_Form = FormRechPartenaire(request.POST,prefix = "RechPart")
        if RechPart_Form.is_valid():
            liste_client = Partenaire.objects.filter(Nom__icontains = RechPart_Form.cleaned_data['nom'])               
    else:
       RechPart_Form = FormRechPartenaire(prefix = "RechPart")


    context = {
        'Titre': titre ,
        'date_resa': request.session.get('date_resa'),
        'nbjours': request.session.get('nbjours'),
        'categorie' : request.session.get('txt_categorie'),
        'vehicule': vehicule,
        'liste_partenaire' : liste_client,
        'FormRechPart' : RechPart_Form,
    }
    request.session['immatriculation'] = immatriculation
    return render(request,'reservation/choixClient.html', context)


@login_required(login_url='/accounts/login/')
def add_driver(request,driver):
    titre = 'Choix du client'
    vehicule = get_object_or_404(Vehicule, pk = request.session.get('immatriculation'))
    liste_client = Partenaire.objects.filter(Nom= '*')
    client = Partenaire.objects.filter(pk= request.session.get('client_fact'))
    conducteur= Partenaire.objects.filter(pk= driver)

    if request.method == 'POST':
       RechPart_Form = FormRechPartenaire(request.POST  ,prefix = "RechPart")
       if RechPart_Form.is_valid():
          liste_client = Partenaire.objects.filter(Nom__icontains=  RechPart_Form.cleaned_data['nom']) 
    else:
       RechPart_Form = FormRechPartenaire(prefix = "RechPart")

    context = {
        'Titre': titre ,
        'date_resa': request.session.get('date_resa'),
        'nbjours': request.session.get('nbjours'),
        'categorie' : request.session.get('txt_categorie'),
        'vehicule': vehicule,
        'liste_partenaire' : liste_client,
        'FormRechPart' : RechPart_Form,
        'conducteur' : conducteur,
        'client' : client,
    }
    request.session['conducteur'] = driver
    return render(request,'reservation/choixClient.html', context)


@login_required(login_url='/accounts/login/')
def add_custumer(request,custumer):
    titre = 'Choix du client'
    vehicule = get_object_or_404(Vehicule, pk=request.session.get('immatriculation'))
    liste_client = Partenaire.objects.filter(Nom= '*')
    client = Partenaire.objects.filter(pk= custumer)
    conducteur= Partenaire.objects.filter(pk= request.session.get('conducteur'))

    if request.method == 'POST':
       RechPart_Form = FormRechPartenaire(request.POST  ,prefix = "RechPart")
       if RechPart_Form.is_valid():
          liste_client = Partenaire.objects.filter(Nom__icontains=  RechPart_Form.cleaned_data['nom']) 
      
    else:
       RechPart_Form = FormRechPartenaire(prefix = "RechPart")

    context = {
        'Titre': titre ,
        'date_resa': request.session.get('date_resa'),
        'nbjours': request.session.get('nbjours'),
        'categorie' : request.session.get('txt_categorie'),
        'vehicule': vehicule,
        'liste_partenaire' : liste_client,
        'FormRechPart' : RechPart_Form,
        'conducteur' : conducteur,
        'client' : client,
    }
    request.session['client_fact'] = custumer
    return render(request,'reservation/choixClient.html', context)


@login_required(login_url='/accounts/login/')
def saveResa(request):
    titre = 'Finaliser'
    vehicule = Vehicule.objects.get( pk= request.session.get('immatriculation'))
    client = Partenaire.objects.get( pk = request.session.get('client_fact'))
    conducteur= Partenaire.objects.get( pk= request.session.get('conducteur'))

    resa = Reservation() 
    resa.debut = datetime.strptime(request.session.get('debut'), "%Y-%m-%d %H:%M:%S")
    resa.Fin = datetime.strptime(request.session.get('fin'), "%Y-%m-%d %H:%M:%S")
    resa.client = client
    resa.conducteur1 = conducteur
    resa.vehicule = vehicule
    resa.save()

    #time_in_datetime = datetime.strptime(time_in_string, "%d-%m-%Y %H:%M:%S")

    context = {
        'Titre': titre ,
        'date_resa': request.session.get('date_resa'),
        'nbjours': request.session.get('nbjours'),
        'categorie' : request.session.get('txt_categorie'),
          }
    
    return render(request,'reservation/choixClient.html', context)



@login_required(login_url='/accounts/login/')
def editResa(request, pk):
    resa = get_object_or_404(Reservation, pk=pk)
    if request.method == "POST":
        form = FormReservation(request.POST, instance=resa)
        if form.is_valid():
            resa = form.save(commit=False)
            resa.save()
            return redirect('reservation:ListeReservation')
    else:
        form = FormReservation(instance=resa)
    context = {
        'titre' : 'Modification réservation',
        'form': form,
        'resa': resa,
        }
    return render(request, 'reservation/editResa.html', context )


@login_required(login_url='/accounts/login/')
def editContrat(request,pk):
    liste_resa = Reservation.objects.filter(pk=pk) 
    resa = liste_resa[0]

    context = {
        'resa': resa ,
          }
    return render(request, 'reservation/msa_contrat_loc/msa_contrat_loc.html', context)

from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Partenaire
from .forms import PartenaireForm, PartFilterForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    liste_partenaire = Partenaire.objects.order_by('Nom')
    if request.method == "POST":
        form = PartFilterForm(request.POST)
        if form.is_valid():
            liste_partenaire = liste_partenaire.filter(Nom__icontains = form.cleaned_data['nom'])
            liste_partenaire = liste_partenaire.filter(Prenom__icontains = form.cleaned_data['prenom'])
            liste_partenaire = liste_partenaire.filter(Telephone__icontains = form.cleaned_data['tel'])
              
    else :
      form = PartFilterForm()



    titre = 'Liste des Partenaires'
    context = {
        'Titre': titre ,
        'Tableau' : '',
        'liste_partenaire': liste_partenaire,
        'form' : form
    }
    return render(request,'partenaire/index.html', context)

@login_required(login_url='/accounts/login/')
def new(request):
    if request.method == "POST":
        form = PartenaireForm(request.POST)
        if form.is_valid():
            partenaire = form.save(commit=False)
            #vehicule.create_by = request.user
            partenaire.save()
            return redirect('partenaire:index')
    else:
        form = PartenaireForm()
    return render(request, 'partenaire/partenaire_edit.html', {'titre' : 'Nouveau partenaire','form': form})

@login_required(login_url='/accounts/login/')
def EditPartenaire(request, pk):
    partenaire = get_object_or_404(Partenaire, pk=pk)
    if request.method == "POST":
        form = PartenaireForm(request.POST, instance=partenaire)
        if form.is_valid():
            partenaire = form.save(commit=False)
            partenaire.save()
            return redirect('partenaire:index')
    else:
        form = PartenaireForm(instance=partenaire)
    return render(request, 'partenaire/partenaire_edit.html', {'titre' : 'Modification partenaire','form': form})
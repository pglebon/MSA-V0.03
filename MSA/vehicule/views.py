from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import Vehicule, Categorie
from .forms import PostForm, formCategorie

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    liste_vehicules = Vehicule.objects.order_by('Immatriculation')
    context = {
        'liste_vehicules': liste_vehicules
    }
    return render(request,'vehicule/index.html', context)

@login_required(login_url='/accounts/login/')
def detail(request, pk):
    vehicule = get_object_or_404(Vehicule, pk=pk)
    return render(request, 'vehicule/detail.html', {'vehicule': vehicule})

@login_required(login_url='/accounts/login/')
def NewVehicule(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            vehicule = form.save(commit=False)
            #vehicule.create_by = request.user
            vehicule.save()
            return redirect('vehicule:detail', pk=vehicule.pk)
    else:
        form = PostForm()
    return render(request, 'vehicule/vehicule_edit.html', {'titre' : 'Nouveau véhicule','form': form})


@login_required(login_url='/accounts/login/')
def EditVehicule(request, pk):
    vehicule = get_object_or_404(Vehicule, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=vehicule)
        if form.is_valid():
            vehicule = form.save(commit=False)
            #vehicule.create_by = request.user
            vehicule.save()
            return redirect('vehicule:detail', pk=vehicule.pk)
    else:
        form = PostForm(instance=vehicule)
    return render(request, 'vehicule/vehicule_edit.html', {'titre' : 'Modification véhicule','form': form})

@login_required(login_url='/accounts/login/')
def listeCategories(request):
    liste_categories = Categorie.objects.order_by('categorie')
    context = {
        'liste_categories': liste_categories
    }
    return render(request,'vehicule/categories.html', context)

@login_required(login_url='/accounts/login/')
def editCategorie(request, pk):
    categorie = get_object_or_404(Categorie, pk=pk)
    if request.method == "POST":
        form = formCategorie(request.POST, instance=categorie)
        if form.is_valid():
            categorie = form.save(commit=False)
            categorie.save()
            return redirect('vehicule:listeCategories')
    else:
        form = formCategorie(instance=categorie)
    return render(request, 'vehicule/categorie_edit.html', {'titre' : 'Modification categorie','form': form})

@login_required(login_url='/accounts/login/')
def newCategorie(request):
    if request.method == "POST":
        form = formCategorie(request.POST)
        if form.is_valid():
            categorie = form.save(commit=False)
            categorie.save()
            return redirect('vehicule:listeCategories')
    else:
        form = formCategorie()
    return render(request, 'vehicule/categorie_edit.html', {'titre' : 'Nouvelle catégorie','form': form})

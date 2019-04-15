from django.shortcuts import render
from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    context = {
        'Tire': 'Accueil'
    }
    return render(request,'home/index.html', context)
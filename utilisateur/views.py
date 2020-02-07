from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from utilisateur.forms import CreerEtudiant, CreerProfesseur
from utilisateur.models import Utilisateur


def creerEtudiant(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreerEtudiant(request.POST)
        # check whether it's valid:
        if form.is_valid():
            prenom = request.POST.get('prenom', '')
            nom = request.POST.get('nom', '')
            email = request.POST.get('email', '')
            numero = request.POST.get('numero', '')
            user = User.objects.create_user(username=numero, password="azerty", first_name=prenom, last_name=nom, email=email)
            Utilisateur.objects.create(user=user, role="Etudiant")
            return HttpResponseRedirect("Bien vu")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreerEtudiant()

    return render(request, 'creerEtudiant.html', {'form': form})


def creerProfesseur(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreerProfesseur(request.POST)
        # check whether it's valid:
        if form.is_valid():
            prenom = request.POST.get('prenom', '')
            nom = request.POST.get('nom', '')
            email = request.POST.get('email', '')
            user = User.objects.create_user(username=email, password="azerty", first_name=prenom, last_name=nom, email=email)
            Utilisateur.objects.create(user=user, role="Professeur")
            return HttpResponseRedirect("Bien vu")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreerProfesseur()

    return render(request, 'creerProfesseur.html', {'form': form})
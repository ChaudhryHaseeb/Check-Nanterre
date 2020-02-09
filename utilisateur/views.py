from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from utilisateur.forms import CreerEtudiant, CreerProfesseur
from utilisateur.models import Utilisateur


def index(request):
    return render(request, 'index.html', {})


def creerEtudiant(request):
    # Si POST, on traite le formulaire
    if request.method == 'POST':
        form = CreerEtudiant(request.POST)
        # Check validite du formulaire
        if form.is_valid():
            prenom = request.POST.get('prenom', '')
            nom = request.POST.get('nom', '')
            email = request.POST.get('email', '')
            numero = request.POST.get('numero', '')
            # password = User.objects.make_random_password()
            password = 'azerty'
            user = User.objects.create_user(username=numero, password=password, first_name=prenom, last_name=nom, email=email)
            Utilisateur.objects.create(user=user, role="Etudiant")
            return HttpResponseRedirect("Bien vu")

    # Si GET, on affiche la page pour remplir le formulaire
    else:
        form = CreerEtudiant()

    return render(request, 'utilisateur/creerEtudiant.html', {'form': form})


def creerProfesseur(request):
    # Si POST, on traite le formulaire
    if request.method == 'POST':
        form = CreerProfesseur(request.POST)
        # Check validite du formulaire
        if form.is_valid():
            prenom = request.POST.get('prenom', '')
            nom = request.POST.get('nom', '')
            email = request.POST.get('email', '')
            # password = User.objects.make_random_password()
            password = 'azerty'
            user = User.objects.create_user(username=email, password=password, first_name=prenom, last_name=nom, email=email)
            Utilisateur.objects.create(user=user, role="Professeur")
            return HttpResponseRedirect("Bien vu")

    # Si GET, on affiche la page pour remplir le formulaire
    else:
        form = CreerProfesseur()

    return render(request, 'utilisateur/creerProfesseur.html', {'form': form})
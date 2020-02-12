from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from rest_framework import viewsets, permissions

from utilisateur.forms import CreerEtudiant, CreerProfesseur, ConnexionForm, MdpOublie
from utilisateur.models import Utilisateur
from django.contrib import messages
from django.core.mail import send_mail

from utilisateur.serializers import UserSerializer, UtilisateurSerializer


def verifSecretaire(user):
    try:
        uti = Utilisateur.objects.get(user=user)
        if uti.role == 'Secretaire':
            return True
        else:
            return False
    except:
        return False


@login_required(login_url="/utilisateur/connexion")
@user_passes_test(verifSecretaire, login_url="/utilisateur/deconnexion")
def index(request):
    # send_mail('Check_Nanterre : Mail test',
    #          'Mail envoyé depuis Django',
    #          'check.nanterre@gmail.com',
    #          ['haseeb.chaudhry@hotmail.fr'])
    return render(request, 'index.html', {})


def connexion(request):
    # Redirection si le user est connecté
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:  # si l'objet retourne n'est pas None
                if Utilisateur.objects.get(user=user).role == 'Secretaire':
                    login(request, user)
                    return render(request, 'index.html')
                else:
                    messages.error(request, "Seul les secretaire peuvent se connecter")
            else:
                messages.error(request, "Email ou mot de passe incorrect")
    else:
        form = ConnexionForm()
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return render(request, 'utilisateur/connexion.html', {'form': form})


def mdpOublie(request):
    if request.method == 'POST':
        form = MdpOublie(request.POST)
        # Check validite du formulaire
        if form.is_valid():
            email = request.POST.get('email', '')
            password = User.objects.make_random_password()
            try:
                # Change mail
                u = User.objects.get(email=email)
                u.set_password(password)
                u.save()
                # Envoi du nouveau mdp par mail
                send_mail('Check_Nanterre : votre nouveau mot de passe',
                          'Bonjour, voici votre nouveau mot de passe pour le site Check_Nanterre : ' + password,
                          'check.nanterre@gmail.com',
                          [email])
                return HttpResponseRedirect('/utilisateur/connexion')
            except:
                messages.error(request, "Email inconnu")
    # Si GET, on affiche la page pour remplir le formulaire
    else:
        form = MdpOublie()
    return render(request, 'utilisateur/mdpOublie.html', {'form': form})


@login_required(login_url="/utilisateur/connexion")
@user_passes_test(verifSecretaire, login_url="/utilisateur/deconnexion")
def creerEtudiant(request):
    # Si POST, on traite le formulaire
    if request.method == 'POST':
        form = CreerEtudiant(request.POST)
        # Check validite du formulaire
        if form.is_valid():
            prenom = request.POST.get('prenom', '')
            nom = request.POST.get('nom', '')
            numero = request.POST.get('numero', '')
            # password = User.objects.make_random_password()
            email = numero + "@parisnanterre.fr"
            password = 'azerty'
            try:
                user = User.objects.create_user(username=numero, password=password, first_name=prenom, last_name=nom,
                                                email=email)
                Utilisateur.objects.create(user=user, role="Etudiant")
                return HttpResponseRedirect("Bien vu")
            except:
                messages.error(request, "Numéro étudiant indisponible")

    # Si GET, on affiche la page pour remplir le formulaire
    else:
        form = CreerEtudiant()
    return render(request, 'utilisateur/creerEtudiant.html', {'form': form})


@login_required(login_url="/utilisateur/connexion")
@user_passes_test(verifSecretaire, login_url="/utilisateur/deconnexion")
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
            try:
                user = User.objects.create_user(username=email, password=password, first_name=prenom, last_name=nom,
                                                email=email)
                Utilisateur.objects.create(user=user, role="Professeur")
                return HttpResponseRedirect("Bien vu")
            except:
                messages.error(request, "Email indisponible")

    # Si GET, on affiche la page pour remplir le formulaire
    else:
        form = CreerProfesseur()

    return render(request, 'utilisateur/creerProfesseur.html', {'form': form})


########################
###### Pour l'API ######
########################
class EtudiantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Utilisateur.objects.all().filter(role='Etudiant')
    serializer_class = UtilisateurSerializer
    permission_classes = (permissions.AllowAny,)


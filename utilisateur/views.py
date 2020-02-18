from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from absence.models import Promotion, PromotionEtudiants
from utilisateur.forms import CreerEtudiant, CreerProfesseur, ConnexionForm, MdpOublie
from utilisateur.models import Utilisateur
from django.contrib import messages
from django.core.mail import send_mail


def verif_secretaire(user):
    try:
        uti = Utilisateur.objects.get(user=user)
        if uti.role == 'Secretaire':
            return True
        else:
            return False
    except:
        return False


@login_required(login_url="/utilisateur/connexion")
@user_passes_test(verif_secretaire, login_url="/utilisateur/deconnexion")
def index(request):
    promotions = Promotion.objects.all()
    return render(request, 'index.html', {'promotions': promotions})


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


def mdp_oublie(request):
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
                return HttpResponseRedirect(reverse('connexion'))
            except:
                messages.error(request, "Email inconnu")
    # Si GET, on affiche la page pour remplir le formulaire
    else:
        form = MdpOublie()
    return render(request, 'utilisateur/mdpOublie.html', {'form': form})


@login_required(login_url="/utilisateur/connexion")
@user_passes_test(verif_secretaire, login_url="/utilisateur/deconnexion")
def creer_etudiant(request):
    # Si POST, on traite le formulaire
    if request.method == 'POST':
        form = CreerEtudiant(request.POST)
        # Check validite du formulaire
        if form.is_valid():
            prenom = request.POST.get('prenom', '')
            nom = request.POST.get('nom', '')
            numero = request.POST.get('numero', '')
            id_promotion = request.POST.get('promotion', '')
            promotion = get_object_or_404(Promotion, pk=id_promotion)
            # password = User.objects.make_random_password()
            email = numero + "@parisnanterre.fr"
            password = 'azerty'
            try:
                user = User.objects.create_user(username=numero, password=password, first_name=prenom, last_name=nom,
                                                email=email)
                util = Utilisateur.objects.create(user=user, role="Etudiant")
                PromotionEtudiants.objects.create(etudiant=util, promotion=promotion)
                messages.success(request, "Ètudiant crée et affecter à une promotion")
            except:
                messages.error(request, "Numéro étudiant indisponible")
            return HttpResponseRedirect(reverse('liste_etudiant'))
    # Si GET, on affiche la page pour remplir le formulaire
    else:
        form = CreerEtudiant()
    return render(request, 'utilisateur/creer_etudiant.html', {'form': form})


@login_required(login_url="/utilisateur/connexion")
@user_passes_test(verif_secretaire, login_url="/utilisateur/deconnexion")
def creer_professeur(request):
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
                messages.success(request, "Professeur crée avec succès !")
            except:
                messages.error(request, "Email indisponible")
            return HttpResponseRedirect(reverse("liste_professeur"))
    # Si GET, on affiche la page pour remplir le formulaire
    else:
        form = CreerProfesseur()
    return render(request, 'utilisateur/creer_professeur.html', {'form': form})


@login_required(login_url="/utilisateur/connexion")
@user_passes_test(verif_secretaire, login_url="/utilisateur/deconnexion")
def liste_etudiant(request):
    liste = Utilisateur.objects.filter(role="Etudiant")
    return render(request, 'utilisateur/liste_etudiant.html', {'liste': liste})


@login_required(login_url="/utilisateur/connexion")
@user_passes_test(verif_secretaire, login_url="/utilisateur/deconnexion")
def modifier_etudiant(request, id_utilisateur):
    user = get_object_or_404(User, pk=id_utilisateur)
    etudiant = Utilisateur.objects.get(user=user)
    etudiant_promotion = PromotionEtudiants.objects.get(etudiant=etudiant.id)
    form = CreerEtudiant(data={'prenom': etudiant.user.first_name, 'nom': etudiant.user.last_name,
                               'numero': etudiant.user.username, 'promotion': etudiant_promotion.promotion})
    if request.method == 'POST':
        form = CreerEtudiant(request.POST)
        if form.is_valid():
            try:
                form.save(etudiant.id)
                messages.success(request, "La modification a été faites avec succès !")
            except:
                messages.error(request, "Erreur dans le formulaire !")
        return HttpResponseRedirect(reverse('liste_etudiant'))
    else:
        return render(request, 'utilisateur/modifier_etudiant.html', {'form': form, 'etudiant': etudiant})


@login_required(login_url="/utilisateur/connexion")
@user_passes_test(verif_secretaire, login_url="/utilisateur/deconnexion")
def liste_professeur(request):
    liste = Utilisateur.objects.filter(role="Professeur")
    return render(request, 'utilisateur/liste_professeur.html', {'liste': liste})


@login_required(login_url="/utilisateur/connexion")
@user_passes_test(verif_secretaire, login_url="/utilisateur/deconnexion")
def modifier_prof(request, id_professeur):
    prof = get_object_or_404(User, pk=id_professeur)
    form = CreerProfesseur(data={'prenom': prof.first_name, 'nom': prof.last_name, 'email': prof.username})
    if request.method == 'POST':
        form = CreerProfesseur(request.POST)
        if form.is_valid():
            try:
                form.save(id_professeur)
                messages.success(request, "Le professeur a bien été modifé !")
            except:
                messages.error(request, "Erreur dans le formulaire !")
        return HttpResponseRedirect(reverse('liste_professeur'))
    else:
        return render(request, 'utilisateur/modifier_professeur.html', {'form': form, 'prof': prof})

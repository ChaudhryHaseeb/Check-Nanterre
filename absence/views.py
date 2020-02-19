import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from absence.forms import CreationMatiere, CreationPromotion
from absence.models import Matiere, Promotion, PromotionEtudiants
from utilisateur.views import verif_secretaire


@login_required(login_url="/utilisateur/connexion")
@user_passes_test(verif_secretaire, login_url="/utilisateur/deconnexion")
def creer_matiere(request):
    if request.method == 'POST':
        form = CreationMatiere(request.POST)
        if form.is_valid():
            try:
                titre = request.POST.get('titre', '')
                Matiere.objects.create(titre=form.cleaned_data['titre'])
                messages.success(request, "Le titre de la matière a été crée avec succès !")
            except:
                messages.error(request, "Erreur dans le formulaire !")
            return HttpResponseRedirect(reverse('liste_matiere'))
    else:
        form = CreationMatiere()
    return render(request, 'creer_matiere.html', {'form': form})


@login_required(login_url="/utilisateur/connexion")
@user_passes_test(verif_secretaire, login_url="/utilisateur/deconnexion")
def liste_matiere(request):
    matieres = Matiere.objects.all()
    return render(request, 'liste_matiere.html', {'matieres': matieres})


@login_required(login_url="/utilisateur/connexion")
@user_passes_test(verif_secretaire, login_url="/utilisateur/deconnexion")
def modifier_matiere(request, id_matiere):
    matiere = get_object_or_404(Matiere, pk=id_matiere)
    form = CreationMatiere(data={'titre': matiere.titre})
    if request.method == 'POST':
        form = CreationMatiere(request.POST)
        if form.is_valid():
            try:
                form.save(id_matiere)
                messages.success(request, "Le titre de la matière a été modifié avec succès !")
            except:
                messages.error(request, "Erreur dans le formulaire !")
        return HttpResponseRedirect(reverse('liste_matiere'))
    else:
        return render(request, 'modifier_matiere.html', {'form': form, 'matiere': matiere})


@login_required(login_url="/utilisateur/connexion")
@user_passes_test(verif_secretaire, login_url="/utilisateur/deconnexion")
def supprimer_matiere(request, id_matiere):
    matiere = get_object_or_404(Matiere, pk=id_matiere)
    try:
        matiere.delete()
        messages.success(request, "La matière a bien été supprimée !")
    except:
        messages.error(request, "Erreur dans la suppression de la matière!")
    return HttpResponseRedirect(reverse('liste_matiere'))


@login_required(login_url="/utilisateur/connexion")
@user_passes_test(verif_secretaire, login_url="/utilisateur/deconnexion")
def creer_promotion(request):
    if request.method == 'POST':
        form = CreationPromotion(request.POST)
        if form.is_valid():
            try:
                nom = request.POST.get('nom', '')
                status = request.POST.get('status', '')
                annee = request.POST.get('annee', '')
                Promotion.objects.create(nom_promotion=nom, status_promotion=status, annee_filiere=annee)
                messages.success(request, "Le titre de la matière a été crée avec succès !")
            except:
                messages.error(request, "Erreur dans le formulaire !")
            return HttpResponseRedirect(reverse('liste_promotion'))
    else:
        form = CreationPromotion()
    return render(request, 'creer_promotion.html', {'form': form})


@login_required(login_url="/utilisateur/connexion")
@user_passes_test(verif_secretaire, login_url="/utilisateur/deconnexion")
def liste_promotion(request):
    promotions = Promotion.objects.all()
    return render(request, 'liste_promotion.html', {'promotions': promotions})


def promotion_contenu(request, id_promotion):
    promotion = get_object_or_404(Promotion, pk=id_promotion)
    promo_etu = PromotionEtudiants.objects.filter(promotion_id=id_promotion)
    return render(request, 'promotion_contenu.html', {'promo_etu': promo_etu, 'promotion': promotion})

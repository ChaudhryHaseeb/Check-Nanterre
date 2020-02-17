from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from absence.forms import CreationMatiere, ModifierMatiere
from absence.models import Matiere
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
    form = ModifierMatiere(data={'titre': matiere.titre})
    if request.method == 'POST':
        form = ModifierMatiere(request.POST)
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

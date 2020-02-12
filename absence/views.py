from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

from absence.forms import CreationMatiere
from absence.models import Matiere
from utilisateur.views import verifSecretaire


@login_required(login_url="/utilisateur/connexion")
@user_passes_test(verifSecretaire, login_url="/utilisateur/deconnexion")
def creer_matiere(request):
    if request.method == 'POST':
        form = CreationMatiere(request.POST)
        if form.is_valid():
            titre = request.POST.get('titre', '')
            Matiere.objects.create(titre=titre)
            print("bien créer")
    else:
        form = CreationMatiere()
    return render(request, 'creer_matiere.html', {'form': form})


@login_required(login_url="/utilisateur/connexion")
@user_passes_test(verifSecretaire, login_url="/utilisateur/deconnexion")
def liste_matiere(request):
    matieres = Matiere.objects.all()
    return render(request, 'liste_matiere.html',{'matieres': matieres})

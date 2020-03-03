import csv
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from absence.forms import CreationMatiere, CreationPromotion, ImportFile
from absence.models import Matiere, Promotion, PromotionEtudiants, Seance, AbsenceEtudiants, SeancePromotion, \
    SeanceProfesseur, SeanceMatiere, AbsenceSeance, Absence
from utilisateur.models import Utilisateur
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


@login_required(login_url="/utilisateur/connexion")
@user_passes_test(verif_secretaire, login_url="/utilisateur/deconnexion")
def promotion_contenu(request, id_promotion):
    promotion = get_object_or_404(Promotion, pk=id_promotion)
    promo_etu = PromotionEtudiants.objects.filter(promotion_id=id_promotion)
    return render(request, 'promotion_contenu.html', {'promo_etu': promo_etu, 'promotion': promotion})


@login_required(login_url="/utilisateur/connexion")
@user_passes_test(verif_secretaire, login_url="/utilisateur/deconnexion")
def liste_seance(request):
    seances = SeancePromotion.objects.all()
    return render(request, 'liste_seance.html', {'seances': seances})


@login_required(login_url="/utilisateur/connexion")
@user_passes_test(verif_secretaire, login_url="/utilisateur/deconnexion")
def liste_absence(request):
    absences = AbsenceEtudiants.objects.all()
    return render(request, 'liste_absence.html', {'absences': absences})


@login_required(login_url="/utilisateur/connexion")
@user_passes_test(verif_secretaire, login_url="/utilisateur/deconnexion")
def liste_seance_absence(request, id_seance):
    seance = get_object_or_404(Seance, pk=id_seance)
    promo = SeancePromotion.objects.get(seance_promotion=seance)
    prof = SeanceProfesseur.objects.get(seance_professeur=seance)
    matiere = SeanceMatiere.objects.get(seance_matiere=seance)
    absent = AbsenceSeance.objects.filter(seance=seance)
    etudiant_absent = []
    for une_absence in absent:
        etudiant_absent.append(AbsenceEtudiants.objects.get(absence_etudiant=une_absence.absence_seance))
    return render(request, 'liste_seance_absence.html', {'seance': seance, 'promo': promo, 'prof': prof,
                                                         'matiere': matiere, 'etudiant_absent': etudiant_absent})


@login_required(login_url="/utilisateur/connexion")
@user_passes_test(verif_secretaire, login_url="/utilisateur/deconnexion")
def absence(request, id_absence):
    absence = get_object_or_404(Absence, pk=id_absence)
    etudiant = AbsenceEtudiants.objects.get(absence_etudiant=absence)
    seance = AbsenceSeance.objects.get(absence_seance=absence)
    matiere = SeanceMatiere.objects.get(seance_matiere=seance.seance)
    prof = SeanceProfesseur.objects.get(seance_professeur=seance.seance)
    return render(request, 'absence.html', {'absence': absence, 'seance': seance, 'matiere': matiere, 'prof': prof,
                                            'etudiant': etudiant})


@login_required(login_url="/utilisateur/connexion")
@user_passes_test(verif_secretaire, login_url="/utilisateur/deconnexion")
def liste_etudiant_absence(request, id_etudiant):
    etudiant = get_object_or_404(Utilisateur, pk=id_etudiant)
    liste_abs = AbsenceEtudiants.objects.filter(etudiant=etudiant)
    liste = []
    for x in liste_abs:
        s = []
        seance = AbsenceSeance.objects.get(absence_seance=x.absence_etudiant)
        s.append(seance)
        liste.append(s)
    return render(request, 'liste_etudiant_absence.html', {'liste': liste, 'etudiant': etudiant})


@login_required(login_url="/utilisateur/connexion")
@user_passes_test(verif_secretaire, login_url="/utilisateur/deconnexion")
def import_file(request, id_promotion):
    promo = get_object_or_404(Promotion, pk=id_promotion)
    if request.method == 'POST':
        form = ImportFile(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            save_csv(file)
            password = "azerty"
            with open('media/import.csv', 'r', encoding='ISO-8859-1', newline='') as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    try:
                        user = User.objects.create_user(username=row[2], password=password, first_name=row[1],
                                                        last_name=row[0], email=row[2]+"@parisnanterre.fr")
                        util = Utilisateur.objects.create(user=user, role="Etudiant")
                        messages.success(request, "L'étudiant {} {} a bien été crée.".format(row[0], row[1]))
                    except:
                        messages.error(request, "Erreur dans la création de l'étudiant {} {}".format(row[0], row[1]))
                    try:
                        PromotionEtudiants.objects.create(etudiant=util, promotion=promo)
                        messages.success(request, "L'étudiant {} {} a bien été affecté à la promotion.".format(row[0], row[1]))
                    except:
                        messages.error(request, "Erreur dans l'affectation de l'étudiant {} {} à une promotion."
                                       .format(row[0], row[1]))
            return HttpResponseRedirect(reverse('promotion_contenu', args=[promo.id]))
    else:
        form = ImportFile()
    return render(request, 'import.html', {'form': form})


def save_csv(f):
    with open('/vagrant/media/import.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

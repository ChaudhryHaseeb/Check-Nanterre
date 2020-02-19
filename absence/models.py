from django.db import models
from django.utils import timezone

from utilisateur.models import Utilisateur


class Promotion(models.Model):
    Licence1 = 'Licence 1'
    Licence2 = 'Licence 2'
    Licence3 = 'Licence 3'
    Master1 = 'Master 1'
    Master2 = 'Master 2'
    NOM_PROMOTION = [
        (Licence1, 'L1'),
        (Licence2, 'L2'),
        (Licence3, 'L3'),
        (Master1, 'M1'),
        (Master2, 'M2'),
    ]
    Classique = 'Classique'
    Apprentissage = 'Apprentissage'
    Mixte = 'Mixte'
    STATUS_PROMOTION = [
        (Classique, 'CLA'),
        (Apprentissage, 'APP'),
        (Mixte, 'MXT'),
    ]
    nom_promotion = models.CharField(max_length=10, choices=NOM_PROMOTION, default="null",)
    annee_filiere = models.CharField(max_length=10, default=str(timezone.now().year) + "-" + str(timezone.now().year+1))
    status_promotion = models.CharField(max_length=13, choices=STATUS_PROMOTION, default="Null")

    def __str__(self):
        return str(self.nom_promotion) + " " + str(self.status_promotion) + " " + str(self.annee_filiere)


class PromotionEtudiants(models.Model):
    etudiant = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.etudiant.user.last_name) + ", " + str(self.promotion.nom_promotion) + " " +\
               str(self.promotion.status_promotion) + " " + str(self.promotion.annee_filiere)


class Matiere(models.Model):
    titre = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.titre)


class MatiereProfesseur(models.Model):
    professeur_matiere = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.professeur_matiere.user.last_name) + ", " + str(self.matiere.titre)


class MatierePromotion(models.Model):
    promotion_matiere = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.promotion_matiere) + ", " + str(self.matiere.titre)


class Seance(models.Model):
    date_seance = models.DateField(null=False, blank=False, default=timezone.now())
    heure_deb = models.TimeField(null=False, blank=False, default=timezone.datetime.strftime(timezone.now(), "%H:%M"))
    heure_fin = models.TimeField(null=False, blank=False, default=timezone.datetime.strftime(timezone.now(), "%H:%M"))

    def __str__(self):
        return str(self.date_seance) + " " + str(self.heure_deb) + str(self.heure_fin)


class SeanceMatiere(models.Model):
    seance_matiere = models.ForeignKey(Seance, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)


class SeanceProfesseur(models.Model):
    seance_professeur = models.ForeignKey(Seance, on_delete=models.CASCADE)
    professeur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)


class SeancePromotion(models.Model):
    seance_promotion = models.ForeignKey(Seance, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE, default="M2")


class Absence(models.Model):

    absent = models.BooleanField(default=False)
    retard = models.IntegerField(default=0)
    justification = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.absent)


class AbsenceEtudiants(models.Model):
    absence_etudiant = models.ForeignKey(Absence, on_delete=models.CASCADE)
    etudiant = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)


class AbsenceSeance(models.Model):
    absence_seance = models.ForeignKey(Absence, on_delete=models.CASCADE)
    seance = models.ForeignKey(Seance, on_delete=models.CASCADE)


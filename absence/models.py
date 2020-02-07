from django.db import models
from django.utils import timezone

from utilisateur.models import Etudiant, Professeur


# Create your models here.


class Promotion(models.Model):
    Licence1 = 'L1'
    Licence2 = 'L2'
    Licence3 = 'L3'
    Master1 = 'M1'
    Master2 = 'M2'
    NOM_PROMOTION = [
        (Licence1, 'Licence 1'),
        (Licence2, 'Licence 2'),
        (Licence3, 'Licence 3'),
        (Master1, 'Master 1'),
        (Master2, 'Master 2'),
    ]
    nom_promotion = models.CharField(max_length=10, choices=NOM_PROMOTION, default="null",)
    annee_filiere = models.CharField(max_length=10, default=str(timezone.now().year) + "-" + str(timezone.now().year+1))
    Classique = 'cla'
    Apprentissage = 'app'
    Mixte = 'mxt'
    STATUS_PROMOTION = [
        (Classique, 'Classique'),
        (Apprentissage, 'Apprentissage'),
        (Mixte, 'Mixte'),
    ]
    status_promotion = models.CharField(
        max_length=3,
        choices=STATUS_PROMOTION,
        default="Null",
    )
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nom_promotion) + " " + str(self.STATUS_PROMOTION) + " " + str(self.annee_filiere)


class Matiere(models.Model):
    """
    TODO Mettre professeur lorsqu'il sera créer
    """
    nom_matiere = models.CharField(max_length=100, blank=False),
    professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nom_matiere)

class Seance(models.Model):
    """
    TODO Rajouter un champs PROFESSEUR
    """
    date_seance = models.DateTimeField(null=True, blank=False)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    promo = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    heure_deb = models.TimeField(null=True, blank=True)
    heure_fin = models.TimeField(null=True, blank=True)

    def __str__(self):
        return str(self.date_seance) + " " + str(self.date_seance) + str(self.promo)

class Absence(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    absent = models.BooleanField(default=False)
    retard = models.IntegerField(default=0)
    justification = models.CharField(max_length=255)
    heure_deb = models.TimeField(null=True, blank=True)
    heure_fin = models.TimeField(null=True, blank=True)
    seance = models.ForeignKey(Seance, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.etudiant) + " " + str(self.absent) + str(self.promo)

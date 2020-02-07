from django.db import models
from django.contrib.auth.models import User


class Etudiant(models.Model):
    # Lien entre l'etudiant et le modele User de django
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    numero_etudiant = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

class Professeur(models.Model):
    """
    TODO Supprimer cette class !!!
    """
    # Lien entre l'etudiant et le modele User de django
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    numero_prof = models.IntegerField(blank=True, null=True)

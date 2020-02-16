from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver


class Utilisateur(models.Model):
    """
    Lien entre l'etudiant et le modele User de django
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ETU = 'Etudiant'
    PROF = 'Professeur'
    SERE = 'Secretaire'
    role_choix = (
        (ETU, 'Etudiant'),
        (PROF, 'Professeur'),
        (SERE, 'Secretaire')
    )
    role = models.CharField(max_length=10, choices=role_choix, default=ETU)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)

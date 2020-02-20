from rest_framework import serializers

from absence.models import Promotion, Absence, Seance, AbsenceSeance, AbsenceEtudiants, Matiere
from utilisateur.api.serializers import UtilisateurSerializer


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields =('id', 'nom_promotion', 'status_promotion', 'annee_filiere')


class AbsenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Absence
        fields =('id', 'absent', 'retard', 'justification')


class SeanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seance
        fields =('id', 'date_seance', 'heure_deb', 'heure_fin')


class AbsenceSeanceSerializer(serializers.ModelSerializer):
    seance = SeanceSerializer()
    absence_seance = AbsenceSerializer()

    class Meta:
        model = AbsenceSeance
        fields = ('id', 'seance', 'absence_seance')


class AbsenceEtudiantsSerializer(serializers.ModelSerializer):
    etudiant = UtilisateurSerializer()
    absence_etudiant = AbsenceSerializer()

    class Meta:
        model = AbsenceEtudiants
        fields = ('id', 'etudiant', 'absence_etudiant')


class MatiereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matiere
        fields = ('id', 'titre')

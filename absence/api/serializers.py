from rest_framework import serializers

from absence.models import Promotion


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields =('id', 'nom_promotion', 'status_promotion', 'annee_filiere')
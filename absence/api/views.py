

# Permet de récupérer l'utilisateur associé à un token
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from absence.api.serializers import PromotionSerializer, AbsenceSeanceSerializer
from absence.models import Promotion, PromotionEtudiants, AbsenceEtudiants, AbsenceSeance, Absence
from utilisateur.api.serializers import UtilisateurSerializer
from utilisateur.models import Utilisateur


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def get_all_promotions(request):
    try:
        promotions = Promotion.objects.all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PromotionSerializer(promotions, many=True)
        return Response(serializer.data)


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def liste_etudiant_dans_promotion(request, id):
    try:
        promo = Promotion.objects.get(id=id)
        promoEtu = PromotionEtudiants.objects.all().filter(promotion=promo)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        listeEtu = []
        for obj in promoEtu:
            listeEtu.append(obj.etudiant)
        serializer = UtilisateurSerializer(listeEtu, many=True)
        return Response(serializer.data)


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def absence_etudiant_connecte(request):
    try:
        user = request.user
        utilisateur = Utilisateur.objects.get(user=user)
        absenceEtu = AbsenceEtudiants.objects.filter(etudiant=utilisateur)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        listeAbsSeance = []
        for obj in absenceEtu:
            listeAbsSeance.append(AbsenceSeance.objects.get(absence_seance=obj.absence_etudiant))
        serializer = AbsenceSeanceSerializer(listeAbsSeance, many=True)
        return Response(serializer.data)


@api_view(['PUT', ])
@permission_classes([IsAuthenticated])
def absence_etudiant_justifier(request, id):
    try:
        abs = Absence.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        data = {}
        try:
            abs.justification = request.data["justification"]
            abs.save()
            data["success"] = "update successful"
            return Response(data=data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)








# Permet de récupérer l'utilisateur associé à un token
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from absence.api.serializers import PromotionSerializer, AbsenceSeanceSerializer
from absence.models import Promotion, PromotionEtudiants, AbsenceEtudiants, AbsenceSeance, Absence, Seance, \
    SeancePromotion, SeanceProfesseur, SeanceMatiere, Matiere
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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def seance_creation(request):
    try:
        util = Utilisateur.objects.get(user=request.user)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "POST":
        if util.role != "Professeur":
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        data = {}
        try:
            seance = Seance.objects.create(date_seance=request.data["date"], heure_deb=request.data["heure_deb"],
                                           heure_fin=request.data["heure_fin"])
            promo = Promotion.objects.get(id=request.data["id_promo"])
            SeancePromotion.objects.create(seance_promotion=seance, promotion=promo)
            SeanceProfesseur.objects.create(seance_professeur=seance, professeur=util)
            matiere = Matiere.objects.get(id=request.data["id_matiere"])
            SeanceMatiere.objects.create(seance_matiere=seance, matiere=matiere)
            data["success"] = "create successful"
            return Response(data=data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)




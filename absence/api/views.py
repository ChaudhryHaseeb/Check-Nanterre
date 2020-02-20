

# Permet de récupérer l'utilisateur associé à un token
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from absence.api.serializers import PromotionSerializer, AbsenceSeanceSerializer, SeanceSerializer, \
    AbsenceEtudiantsSerializer, MatiereSerializer
from absence.models import Promotion, PromotionEtudiants, AbsenceEtudiants, AbsenceSeance, Absence, Seance, \
    SeancePromotion, SeanceProfesseur, SeanceMatiere, Matiere, MatiereProfesseur
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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def absence_creation(request):
    try:
        util = Utilisateur.objects.get(user=request.user)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "POST":
        if util.role != "Professeur":
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        data = {}
        try:
            absence = Absence.objects.create(absent=request.data["absence"], retard=request.data["retard"],
                                             justification="")
            seance = Seance.objects.get(id=request.data["id_seance"])
            AbsenceSeance.objects.create(absence_seance=absence, seance=seance)
            etu = Utilisateur.objects.get(id = request.data["id_etudiant"])
            AbsenceEtudiants.objects.create(absence_etudiant=absence, etudiant=etu)
            data["success"] = "create successful"
            return Response(data=data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def absence_professeur_update(request):
    try:
        util = Utilisateur.objects.get(user=request.user)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "POST":
        if util.role != "Professeur":
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        data = {}
        try:
            absence = Absence.objects.create(absent=request.data["absence"], retard=request.data["retard"],
                                             justification="")
            seance = Seance.objects.get(id=request.data["id_seance"])
            AbsenceSeance.objects.create(absence_seance=absence, seance=seance)
            etu = Utilisateur.objects.get(id = request.data["id_etudiant"])
            AbsenceEtudiants.objects.create(absence_etudiant=absence, etudiant=etu)
            data["success"] = "create successful"
            return Response(data=data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', ])
@permission_classes([IsAuthenticated])
def absence_modifier(request, id):
    try:
        abs = Absence.objects.get(id=id)
        util = Utilisateur.objects.get(user=request.user)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        if util.role != "Professeur":
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        data = {}
        try:
            abs.absent = request.data["absence"]
            abs.retard = request.data["retard"]
            abs.save()
            data["success"] = "update successful"
            return Response(data=data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def list_seance_prof(request):
    try:
        util = Utilisateur.objects.get(user=request.user)
        sceanceProf = SeanceProfesseur.objects.filter(professeur=util)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        if util.role != "Professeur":
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        listeSeance = []
        for obj in sceanceProf:
            listeSeance.append(obj.seance_professeur)
        serializer = SeanceSerializer(listeSeance, many=True)
        return Response(serializer.data)


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def list_etudiant_seance(request, id):
    try:
        util = Utilisateur.objects.get(user=request.user)
        seance = Seance.objects.get(id=id)
        seancePromo = SeancePromotion.objects.get(seance_promotion=seance)
        promo = Promotion.objects.get(id=seancePromo.promotion.id)
        promoEtu = PromotionEtudiants.objects.all().filter(promotion=promo)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        if util.role != "Professeur":
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        listeEtu = []
        for obj in promoEtu:
            listeEtu.append(obj.etudiant)
        serializer = UtilisateurSerializer(listeEtu, many=True)
        return Response(serializer.data)


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def list_etudiant_absent_seance(request, id):
    try:
        util = Utilisateur.objects.get(user=request.user)
        seance = Seance.objects.get(id=id)
        absenceSeance = AbsenceSeance.objects.filter(seance=seance)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        if util.role != "Professeur":
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        listeAbs = []
        for obj in absenceSeance:
            listeAbs.append(AbsenceEtudiants.objects.get(absence_etudiant=obj.absence_seance))

        serializer = AbsenceEtudiantsSerializer(listeAbs, many=True)
        return Response(serializer.data)


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def list_matiere(request):
    try:
        listeMatiere = Matiere.objects.all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":

        serializer = MatiereSerializer(listeMatiere, many=True)
        return Response(serializer.data)


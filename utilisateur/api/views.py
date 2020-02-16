from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User

from utilisateur.api.serializers import UtilisateurSerializer, UserSerializer
from utilisateur.models import Utilisateur


# Permet de récupérer l'utilisateur associé à un token
@api_view(['GET', ])
def user_connecte(request):
    try:
        utilisateur = Utilisateur.objects.get(user=request.user)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UtilisateurSerializer(utilisateur)
        return Response(serializer.data)
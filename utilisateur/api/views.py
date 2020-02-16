from django.core.mail import send_mail
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


@api_view(['PUT',])
def user_modifier_mdp(request):
    try:
        user = request.user
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "PUT":
        data = {}
        try:
            user.set_password(request.data["password"])
            user.save()
            data["success"] = "update successful"
            return Response(data=data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT',])
def user_reset_mdp(request):
    try:
        user = User.objects.get(email=request.data["email"])
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "PUT":
        data = {}
        try:
            password = User.objects.make_random_password()
            user.set_password(password)
            user.save()
            # Envoi du nouveau mdp par mail
            send_mail('Check_Nanterre : votre nouveau mot de passe',
                      'Bonjour, voici votre nouveau mot de passe pour le site Check_Nanterre : ' + password,
                      'check.nanterre@gmail.com',
                      [request.data["email"]])
            data["success"] = "update successful"
            return Response(data=data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
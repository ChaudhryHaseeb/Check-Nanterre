from django.contrib.auth.models import User
from rest_framework import serializers

from utilisateur.models import Utilisateur


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('id', 'username', 'first_name', 'last_name', 'email', 'last_login')


class UtilisateurSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Utilisateur
        fields = ['role', 'user']
